from pydantic import BaseModel,Field
class ReviewAnalyzer(BaseModel):
    summary:str =Field(description="Give a brief and precise summary of the review")
    sentiment:str =Field(description="Return only positive,negative or neutral ")
    rating:int=Field(description="Return an integer rating from 1 to 5")
    confidence:float=Field(description="Return a confidence score between 0 and 1")
    positive_points:list[str]=Field(description="List of all the positive points")
    negative_points:list[str]=Field(description="list of all the negative points")
    recommendation:str=Field(description="Return either Recommended or Not Recommneded")