from typing_extensions import TypedDict,Annotated,Optional
class reviewAnalyzer(TypedDict):
    summary:Annotated[str,"Here give a breif and preceise summary of the review"]
    sentiment:str
    rating:int
    confidence:float
    positive_points=Annotated[list[str],"Here give the positive points of the review"]
    negative_points=Annotated[list[str],"Here give the negative points of the review"]
    recommedation=str
