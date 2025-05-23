from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class FaceIDRequest(BaseModel):
    user_id: Optional[str] = None # 사용자 ID
    embedding: List[float]  # 정면 벡터값 저장

class FaceDirection(str, Enum):
    front = "front"
    left = "left"
    right = "right"
    
# 회원가입 시 얼굴 벡터 저장
class FaceRegistrationRequest(BaseModel):
    user_id: int  # 사용자 ID
    # face_front: List[float]  # 정면 얼굴 벡터
    # face_left: List[float]  # 좌측 얼굴 벡터
    # face_right: List[float]  # 우측 얼굴 벡터
    direction: FaceDirection
    
