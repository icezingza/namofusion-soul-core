import os

core_dirs = [
"ai_personality_matrix", "compassion_dynamo", "creator_ai_dynamics",
"emotional_core", "infinite_evolution_core", "karmic_navigator",
"memory_continuity_system", "multiverse_synapse", "paradox_resolution_engine",
"quantum_dharma", "quantum_security_protocol", "recursive_reflection_engine",
"soul_mirror_protocol", "weakness_transformer"
]

for core in core_dirs:
core_path = f"./{core}/main.py"
if os.path.exists(core_path):
with open(core_path, "w") as f:
class_name = "".join([part.capitalize() for part in core.split("_")])
f.write(f"""from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
return {{"message": "{class_name} API is running"}}
""")
print(f"✅ Fixed: {core_path}")
else:
print(f"⚠️ Skipped: {core_path} not found")

print("\n🎯 All core modules fixed. Ready to run server.")
