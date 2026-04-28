from pydantic import BaseModel, Field
from enum import Enum

class Education(str, Enum):
    graduate = "Graduate"
    not_graduate = "Not Graduate"

class Employment(str, Enum):
    yes = "Yes"
    no = "No"

class InputData(BaseModel):
    no_of_dependents: int = Field(..., description="Number of dependents (0-5)")
    education: Education
    self_employed: Employment
    income_annum: float = Field(..., description="Annual income")
    loan_amount: float = Field(..., description="Loan amount")
    loan_term: int = Field(..., description="Loan term (years)")
    cibil_score: int = Field(..., ge=300, le=900, description="Credit score (300-900)")
    residential_assets_value: float
    commercial_assets_value: float
    luxury_assets_value: float
    bank_asset_value: float