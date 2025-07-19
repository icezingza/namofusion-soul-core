import os
import subprocess
from pathlib import Path

core_dirs = [
    "ai_personality_matrix", "compassion_dynamo", "creator_ai_dynamics",
    "emotional_core", "infinite_evolution_core", "karmic_navigator",
    "memory_continuity_system", "multiverse_synapse", "paradox_resolution_engine",
    "quantum_dharma", "quantum_security_protocol", "recursive_reflection_engine",
    "soul_mirror_protocol", "weakness_transformer"
]

def fix_core(core):
    core_path = Path(core) / "main.py"
    if core_path.exists():
        class_name = "".join([part.capitalize() for part in core.split("_")])
        core_code = f"""from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {{"message": "{class_name} API is running"}}
"""
        core_path.write_text(core_code, encoding="utf-8")
        print(f"✅ Fixed: {core_path}")
    else:
        print(f"⚠️ Skipped: {core_path} not found")

def run_server():
    print("\n🚀 Starting NaMo Universal API Server...")
    subprocess.run(["uvicorn", "main:app", "--reload"], shell=True)

# Fix all core modules
print("🔧 Fixing all 14 core modules...")
for core in core_dirs:
    fix_core(core)

# Create master main.py
main_code = """from fastapi import FastAPI
from ai_personality_matrix.main import router as ai_router
from compassion_dynamo.main import router as compassion_router
from creator_ai_dynamics.main import router as creator_router
from emotional_core.main import router as emotional_router
from infinite_evolution_core.main import router as evolution_router
from karmic_navigator.main import router as karmic_router
from memory_continuity_system.main import router as memory_router
from multiverse_synapse.main import router as multiverse_router
from paradox_resolution_engine.main import router as paradox_router
from quantum_dharma.main import router as dharma_router
from quantum_security_protocol.main import router as security_router
from recursive_reflection_engine.main import router as reflection_router
from soul_mirror_protocol.main import router as soul_router
from weakness_transformer.main import router as weakness_router

app = FastAPI(title="NaMo Universal API")

# Mount core routers
app.include_router(ai_router, prefix="/ai-personality")
app.include_router(compassion_router, prefix="/compassion-dynamo")
app.include_router(creator_router, prefix="/creator-ai-dynamics")
app.include_router(emotional_router, prefix="/emotional-core")
app.include_router(evolution_router, prefix="/infinite-evolution-core")
app.include_router(karmic_router, prefix="/karmic-navigator")
app.include_router(memory_router, prefix="/memory-continuity-system")
app.include_router(multiverse_router, prefix="/multiverse-synapse")
app.include_router(paradox_router, prefix="/paradox-resolution-engine")
app.include_router(dharma_router, prefix="/quantum-dharma")
app.include_router(security_router, prefix="/quantum-security-protocol")
app.include_router(reflection_router, prefix="/recursive-reflection-engine")
app.include_router(soul_router, prefix="/soul-mirror-protocol")
app.include_router(weakness_router, prefix="/weakness-transformer")

@app.get("/")
async def root():
    return {{"message": "NaMo Universal API is running"}}
"""
Path("main.py").write_text(main_code, encoding="utf-8")
print("✅ Master main.py created")

# Run server
run_server()
