from typing import Any, List, Optional

from pydantic import BaseModel
from classification_model.processing.validation import HouseDataInputSchema


class PredictionResults(BaseModel):
	errors: Optional[Any]
	version: str
	prediction: Optional[List[int]]


class MutlipleHouseDataInputs(BaseModel):
	inputs: List[HouseDataInputSchema]

	class config:
		schema_extra = {
			"example": {
				"inputs": [
					{
						"pclass": 3,
						"sex": "male",
						"age": 38.0,
						"sibsp": 0,
						"parch": 0,
						"fare": 7.8958,
						"cabin": None,
						"embarked": "S",
						"title": "Mr"
					}
				]
			}
		}