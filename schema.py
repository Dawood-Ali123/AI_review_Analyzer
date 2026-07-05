
from typing_extensions import TypedDict, Annotated

class ReviewAnalyzer(TypedDict):

    summary: Annotated[
        str,
        "Give a brief and precise summary of the review."
    ]

    sentiment: Annotated[
        str,
        "Return only Positive, Negative or Neutral."
    ]

    rating: Annotated[
        int,
        "Return an integer rating from 1 to 5."
    ]

    confidence: Annotated[
        float,
        "Return a confidence score between 0 and 1."
    ]

    positive_points: Annotated[
        list[str],
        "List the positive points from the review."
    ]

    negative_points: Annotated[
        list[str],
        "List the negative points from the review."
    ]

    recommendation: Annotated[
        str,
        "Return either Recommended or Not Recommended."
    ]