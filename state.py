from typing import Annotated, Literal, Optional
from typing_extensions import TypedDict
from langgraph.graph.message import AnyMessage, add_messages


class StatePartOne(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    user_info: str


class StatePartTwo(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    user_info: str


class StatePartThree(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    user_info: str


def update_dialog_stack(left: list[str], right: Optional[str]) -> list[str]:
    """Push or pop the state."""
    if right is None:
        return left
    if right == "pop":
        return left[:-1]
    return left + [right]


class StatePartFour(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    user_info: str
    dialog_state: Annotated[
        list[
            Literal[
                "assistant",
                "update_flight",
                "book_car_rental",
                "book_hotel",
                "book_excursion",
            ]
        ],
        update_dialog_stack,
    ]
