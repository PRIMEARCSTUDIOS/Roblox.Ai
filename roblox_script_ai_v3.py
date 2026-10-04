
# =========================================================
# 🎮 ROBLOX SCRIPT AI ASSISTANT v3.0
# =========================================================

import random
import time
import textwrap

titles = [
    "🎮 ROBLOX SCRIPT AI ASSISTANT  v3.0",
    "🚀 ROBLOX LUA GENERATOR  v3.0",
    "🧠 ROBLOX DEV AI TERMINAL  v3.0"
]

subtitles = [
    "Tell me what you want - I'll generate Roblox Lua code!",
    "Describe your Roblox idea and get a script instantly!",
    "Write your Roblox system idea below!"
]

print("\n" + "=" * 70)
print("   " + random.choice(titles))
print("   " + random.choice(subtitles))
print("=" * 70)

help_menu = '''
╔════════════════════════════════════════════════════════════╗
║                 🎮 ROBLOX AI SYSTEMS MENU                 ║
╠════════════════════════════════════════════════════════════╣
║ kill brick                leaderboard                     ║
║ speed boost               teleport system                 ║
║ tool giver                double jump                     ║
║ sprint system             invisibility                    ║
║ flying system             npc dialogue                    ║
║ zombie ai                 checkpoint system               ║
║ and many more systems...                                  ║
╚════════════════════════════════════════════════════════════╝

📌 COMMANDS:
• help  -> show this menu
• quit  -> exit program
'''

thinking = [
    "🧠 Understanding your Roblox system...",
    "⚡ Generating optimized Lua code...",
    "🚀 Building Roblox script..."
]

success = [
    "✅ Script generated successfully!",
    "🔥 Lua code ready!"
]

scripts = {

"kill brick": {
"place": "📍 Put this Script inside the Part that kills players.",
"code": '''
local brick = script.Parent

brick.Touched:Connect(function(hit)

    local humanoid = hit.Parent:FindFirstChild("Humanoid")

    if humanoid then
        humanoid.Health = 0
    end

end)
'''
},

"speed boost": {
"place": "📍 Put this Script inside a Part in Workspace.",
"code": '''
local part = script.Parent

part.Touched:Connect(function(hit)

    local humanoid = hit.Parent:FindFirstChild("Humanoid")

    if humanoid then
        humanoid.WalkSpeed = 40
    end

end)
'''
},

"leaderboard": {
"place": "📍 Put this Script inside ServerScriptService.",
"code": '''
game.Players.PlayerAdded:Connect(function(player)

    local leaderstats = Instance.new("Folder")
    leaderstats.Name = "leaderstats"
    leaderstats.Parent = player

end)
'''
}

}

def detect(user):

    user = user.lower()

    if "kill" in user:
        return "kill brick"

    elif "speed" in user:
        return "speed boost"

    elif "leaderboard" in user:
        return "leaderboard"

    return None

while True:

    user = input("\n🎮 You: ")

    if user.lower() == "quit":
        print("\n👋 Thanks for using ROBLOX SCRIPT AI ASSISTANT v3.0")
        break

    if user.lower() == "help":
        print(help_menu)
        continue

    print("\n" + random.choice(thinking))
    time.sleep(1)

    result = detect(user)

    if result:

        data = scripts[result]

        print("\n" + random.choice(success))
        print("=" * 70)

        print("\n🎯 SYSTEM DETECTED:")
        print(result.upper())

        print("\n📌 WHERE TO PUT THE SCRIPT:")
        print(data["place"])

        print("\n📜 LUA SCRIPT:")
        print("-" * 70)

        print(textwrap.dedent(data["code"]))

        print("-" * 70)

    else:

        print("\n❌ I couldn't understand your request.")
