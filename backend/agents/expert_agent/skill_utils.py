from typing import List, Dict

from langchain_core.output_parsers import PydanticOutputParser
from langchain_groq import ChatGroq
from pydantic import BaseModel

from config.settings import GROQ_API_KEY

from sqlalchemy.orm import Session

from db.crud import get_employees_by_skills

class SkillExtraction(BaseModel):
    skills: List[str]


def skill_extractor_tool(query: str) -> List[str]:
    llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)

    prompt = (
        "Extract ONLY technical skills or relevant expertise from the user query. "
        'Return valid JSON **using double quotes** exactly like this: {"skills": ["skill1", "skill2"]}. '
        "Do NOT include any explanations, markdown, or formatting. "
        "Expand abbreviations (e.g. 'k8s' → 'kubernetes'). "
        'If no skills exist, return {"skills": []}.\n\n'
        f"User query: {query}"
    )

    parser = PydanticOutputParser(pydantic_object=SkillExtraction)
    response = llm.invoke(
        [
            {"role": "system", "content": prompt},
        ]
    )

    parsed = parser.parse(response.content)
    return [skill.lower() for skill in parsed.skills]


def skill_lookup_tool(db: Session, skills: List[str]) -> Dict:
    if not skills:
        return {"employees": []}

    employees = get_employees_by_skills(db, skills)

    if not employees:
        return {"employees": []}

    result = []
    for emp in employees:
        if emp.position_obj:
            result.append(
                {
                    "full_name": emp.full_name,
                    "email": emp.email,
                    "department": emp.department,
                    "position_level": emp.position_obj.position_level,
                    "position": emp.position_obj.position,
                    "skills": emp.position_obj.skills,
                }
            )

    return {"employees": result}
