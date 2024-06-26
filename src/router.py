from fastapi import APIRouter

from src.documents.routers import documents_v1_router
from src.tests.routers import tests_v1_router
from src.users.routers import user_v1_router


router_v1 = APIRouter()

router_v1.include_router(tests_v1_router, prefix='/tests')
router_v1.include_router(documents_v1_router, prefix='/documents')
router_v1.include_router(user_v1_router, prefix='/users')
