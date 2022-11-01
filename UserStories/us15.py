from Classes.Individual import Individual
from Classes.Family import Family
from typing import List, Dict

def fewer_than_15_siblings(siblings: List[str]) -> bool:
    """_summary_

    Args:
        siblings (List[str]): _description_

    Raises:
        Exception: _description_

    Returns:
        bool: _description_
    """
    
    if len(siblings) < 15:
        return True
    else:
        raise Exception("has more then 15 siblings")