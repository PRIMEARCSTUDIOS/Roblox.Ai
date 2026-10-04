# ============================================================
#  🎮 Roblox Script AI Assistant
#  Run this with: python RobloxAI.py
#  Type your request in plain English → Get Lua code instantly
# ============================================================

import re

# ============================================================
# 🧠 INTENT MAP, Keywords → Intent
# ============================================================

INTENT_MAP = {
    "kill_brick":       ["kill brick", "kill", "deadly", "damage brick", "lava", "death brick"],
    "leaderboard":      ["leaderboard", "stats", "points", "score", "cash", "coins", "money"],
    "teleport":         ["teleport", "tp pad", "warp", "move player", "teleport pad"],
    "speed_boost":      ["speed boost", "speed", "fast", "run faster", "walkspeed"],
    "door":             ["door", "open door", "proximity door", "gate", "entrance"],
    "jump_boost":       ["jump boost", "jump", "high jump", "jump power", "super jump"],
    "reset_player":     ["reset player", "reset", "respawn", "kill player"],
    "gui_message":      ["gui", "message", "screen message", "show text", "display text", "welcome message"],
    "tool_giver":       ["tool giver", "give tool", "weapon", "sword", "give item", "item giver"],
    "admin_check":      ["admin", "admin check", "is admin", "owner check"],
    "shop":             ["shop", "buy", "purchase", "store", "buy item"],
    "checkpoint":       ["checkpoint", "save point", "save progress", "respawn point"],
    "timer":            ["timer", "countdown", "time left", "clock"],
    "day_night":        ["day night", "day cycle", "night cycle", "lighting", "time of day"],
    "vehicle_spawn":    ["vehicle", "car", "spawn car", "spawn vehicle", "drive"],
    "chat_command":     ["chat command", "command", "!speed", "!jump", "!tp", "player command"],
    "npc_dialog":       ["npc", "dialog", "npc talk", "npc message", "talk to npc"],
    "invisibility":     ["invisible", "invisibility", "hide player", "transparency"],
    "forcefield":       ["forcefield", "force field", "shield", "protect player", "invincible"],
    "music_player":     ["music", "play music", "sound", "background music", "audio"],
    "datastore":        ["datastore", "save data", "load data", "persistent data", "save stats"],
    "tween_move":       ["tween", "smooth move", "animate part", "moving platform", "slide"],
    "explosion":        ["explosion", "explode", "blast", "boom"],
    "random_teleport":  ["random teleport", "random spawn", "random position"],
    "team_system":      ["team", "teams", "join team", "team system", "red team", "blue team"],
}

# ============================================================
# 📜 LUA SCRIPT TEMPLATES
# ============================================================

SCRIPTS = {

"kill_brick": """
-- 🔴 KILL BRICK SCRIPT
-- Place this Script inside a Part in Workspace

local part = script.Parent

part.Touched:Connect(function(hit)
    local character = hit.Parent
    local humanoid = character:FindFirstChildOfClass("Humanoid")
    if humanoid then
        humanoid.Health = 0
    end
end)
""",

"leaderboard": """
-- 🏆 LEADERBOARD SCRIPT
-- Place this Script inside ServerScriptService

local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
    local leaderstats = Instance.new("Folder")
    leaderstats.Name = "leaderstats"
    leaderstats.Parent = player

    local cash = Instance.new("IntValue")
    cash.Name = "Cash"
    cash.Value = 0
    cash.Parent = leaderstats

    local level = Instance.new("IntValue")
    level.Name = "Level"
    level.Value = 1
    level.Parent = leaderstats
end)
""",

"teleport": """
-- 🌀 TELEPORT PAD SCRIPT
-- Place this Script inside a Part in Workspace
-- Edit TARGET_POSITION to change destination

local part = script.Parent
local TARGET_POSITION = Vector3.new(0, 10, 0) -- ✏️ Change this!
local debounce = false

part.Touched:Connect(function(hit)
    if debounce then return end
    local character = hit.Parent
    local humanoid = character:FindFirstChildOfClass("Humanoid")
    if humanoid then
        debounce = true
        local root = character:FindFirstChild("HumanoidRootPart")
        if root then
            root.CFrame = CFrame.new(TARGET_POSITION)
        end
        task.wait(1)
        debounce = false
    end
end)
""",

"speed_boost": """
-- ⚡ SPEED BOOST SCRIPT
-- Place this Script inside a Part in Workspace

local part = script.Parent
local BOOST_SPEED = 50      -- ✏️ Default is 16
local BOOST_DURATION = 5    -- ✏️ Seconds
local debounce = false

part.Touched:Connect(function(hit)
    if debounce then return end
    local character = hit.Parent
    local humanoid = character:FindFirstChildOfClass("Humanoid")
    if humanoid then
        debounce = true
        humanoid.WalkSpeed = BOOST_SPEED
        task.wait(BOOST_DURATION)
        humanoid.WalkSpeed = 16
        debounce = false
    end
end)
""",

"door": """
-- 🚪 PROXIMITY DOOR SCRIPT
-- Place this Script inside your Door Part

local door = script.Parent
local isOpen = false
local OPEN_OFFSET = Vector3.new(0, 10, 0) -- ✏️ Direction door moves

local prompt = Instance.new("ProximityPrompt")
prompt.ActionText = "Open"
prompt.ObjectText = "Door"
prompt.HoldDuration = 0
prompt.Parent = door

prompt.Triggered:Connect(function()
    if not isOpen then
        isOpen = true
        prompt.ActionText = "Close"
        door.CFrame = door.CFrame + OPEN_OFFSET
    else
        isOpen = false
        prompt.ActionText = "Open"
        door.CFrame = door.CFrame - OPEN_OFFSET
    end
end)
""",

"jump_boost": """
-- 🦘 JUMP BOOST SCRIPT
-- Place this Script inside a Part in Workspace

local part = script.Parent
local BOOST_POWER = 100     -- ✏️ Default is 50
local BOOST_DURATION = 5    -- ✏️ Seconds
local debounce = false

part.Touched:Connect(function(hit)
    if debounce then return end
    local character = hit.Parent
    local humanoid = character:FindFirstChildOfClass("Humanoid")
    if humanoid then
        debounce = true
        humanoid.JumpPower = BOOST_POWER
        task.wait(BOOST_DURATION)
        humanoid.JumpPower = 50
        debounce = false
    end
end)
""",

"reset_player": """
-- 💀 RESET PLAYER SCRIPT
-- Place this Script inside a Part in Workspace

local part = script.Parent

part.Touched:Connect(function(hit)
    local character = hit.Parent
    local humanoid = character:FindFirstChildOfClass("Humanoid")
    if humanoid then
        humanoid.Health = 0
    end
end)
""",

"gui_message": """
-- 💬 GUI WELCOME MESSAGE SCRIPT
-- Place this Script inside ServerScriptService

local Players = game:GetService("Players")

local function showMessage(player, text)
    local gui = Instance.new("ScreenGui")
    gui.Parent = player.PlayerGui

    local frame = Instance.new("Frame")
    frame.Size = UDim2.new(0.5, 0, 0.1, 0)
    frame.Position = UDim2.new(0.25, 0, 0.1, 0)
    frame.BackgroundColor3 = Color3.fromRGB(0, 0, 0)
    frame.BackgroundTransparency = 0.4
    frame.Parent = gui

    local label = Instance.new("TextLabel")
    label.Size = UDim2.new(1, 0, 1, 0)
    label.BackgroundTransparency = 1
    label.TextColor3 = Color3.fromRGB(255, 255, 255)
    label.TextScaled = true
    label.Text = text
    label.Font = Enum.Font.GothamBold
    label.Parent = frame

    task.wait(3)
    gui:Destroy()
end

Players.PlayerAdded:Connect(function(player)
    task.wait(1)
    showMessage(player, "Welcome to the game! 🎮")
end)
""",

"tool_giver": """
-- 🗡️ TOOL GIVER SCRIPT
-- 1. Place your Tool inside ServerStorage
-- 2. Place this Script inside a Part
-- 3. Change TOOL_NAME to your tool's exact name

local part = script.Parent
local ServerStorage = game:GetService("ServerStorage")
local TOOL_NAME = "Sword" -- ✏️ Change this to your tool's name!
local debounce = false

part.Touched:Connect(function(hit)
    if debounce then return end
    local character = hit.Parent
    local player = game.Players:GetPlayerFromCharacter(character)
    if player then
        local tool = ServerStorage:FindFirstChild(TOOL_NAME)
        if tool and not player.Backpack:FindFirstChild(TOOL_NAME) then
            debounce = true
            tool:Clone().Parent = player.Backpack
            task.wait(1)
            debounce = false
        end
    end
end)
""",

"admin_check": """
-- 🛡️ ADMIN SYSTEM SCRIPT
-- Place this Script inside ServerScriptService
-- Add admin usernames to the ADMINS table

local ADMINS = {
    "YourUsername",    -- ✏️ Replace with your Roblox username
    "FriendUsername",  -- Add more admins below
}

local function isAdmin(player)
    for _, name in ipairs(ADMINS) do
        if player.Name == name then return true end
    end
    return false
end

game.Players.PlayerAdded:Connect(function(player)
    if isAdmin(player) then
        print(player.Name .. " joined as ADMIN ✅")
        -- Add your admin powers here
    else
        print(player.Name .. " is a regular player.")
    end
end)
""",

"shop": """
-- 🛒 BASIC SHOP SCRIPT
-- Place inside ServerScriptService
-- Uses leaderstats Cash as currency

local Players = game:GetService("Players")

local SHOP_ITEMS = {
    {name = "Speed Boost", price = 50, stat = "WalkSpeed", value = 32},
    {name = "Jump Boost",  price = 75, stat = "JumpPower",  value = 100},
}

local function buyItem(player, itemName)
    local leaderstats = player:FindFirstChild("leaderstats")
    if not leaderstats then return print("No leaderstats found!") end
    local cash = leaderstats:FindFirstChild("Cash")
    if not cash then return end

    for _, item in ipairs(SHOP_ITEMS) do
        if item.name == itemName then
            if cash.Value >= item.price then
                cash.Value = cash.Value - item.price
                local humanoid = player.Character and player.Character:FindFirstChildOfClass("Humanoid")
                if humanoid then
                    humanoid[item.stat] = item.value
                end
                print(player.Name .. " bought: " .. item.name)
            else
                print(player.Name .. " cannot afford: " .. item.name)
            end
        end
    end
end

-- Example usage (call from a RemoteEvent or proximity prompt):
-- buyItem(player, "Speed Boost")
""",

"checkpoint": """
-- 🚩 CHECKPOINT SYSTEM
-- Place a Script inside each checkpoint Part
-- Saves the player's spawn to that checkpoint

local checkpoint = script.Parent
local debounce = {}

checkpoint.Touched:Connect(function(hit)
    local character = hit.Parent
    local player = game.Players:GetPlayerFromCharacter(character)
    if player and not debounce[player.UserId] then
        debounce[player.UserId] = true
        player.RespawnLocation = checkpoint
        print(player.Name .. " reached checkpoint: " .. checkpoint.Name)
        task.wait(1)
        debounce[player.UserId] = false
    end
end)
""",

"timer": """
-- ⏱️ COUNTDOWN TIMER SCRIPT
-- Place inside ServerScriptService
-- Broadcasts timer to all players via a GUI

local Players = game:GetService("Players")
local TIME_LIMIT = 60 -- ✏️ Seconds

local function updateTimerGui(timeLeft)
    for _, player in ipairs(Players:GetPlayers()) do
        local gui = player.PlayerGui:FindFirstChild("TimerGui")
        if gui then
            local label = gui:FindFirstChild("TimerLabel", true)
            if label then
                label.Text = "⏱️ Time Left: " .. timeLeft .. "s"
            end
        end
    end
end

local function createTimerGui(player)
    local gui = Instance.new("ScreenGui")
    gui.Name = "TimerGui"
    gui.Parent = player.PlayerGui

    local label = Instance.new("TextLabel")
    label.Name = "TimerLabel"
    label.Size = UDim2.new(0.2, 0, 0.05, 0)
    label.Position = UDim2.new(0.4, 0, 0, 10)
    label.BackgroundTransparency = 1
    label.TextColor3 = Color3.fromRGB(255, 255, 255)
    label.TextScaled = true
    label.Font = Enum.Font.GothamBold
    label.Text = "⏱️ Time Left: " .. TIME_LIMIT .. "s"
    label.Parent = gui
end

Players.PlayerAdded:Connect(createTimerGui)

-- Start countdown
task.spawn(function()
    for t = TIME_LIMIT, 0, -1 do
        updateTimerGui(t)
        task.wait(1)
    end
    print("⏱️ Time is up!")
end)
""",

"day_night": """
-- 🌅 DAY/NIGHT CYCLE SCRIPT
-- Place inside ServerScriptService

local Lighting = game:GetService("Lighting")
local CYCLE_SPEED = 60 -- ✏️ Seconds per full day cycle

task.spawn(function()
    while true do
        for hour = 0, 24, 0.1 do
            Lighting.TimeOfDay = string.format("%02d:%02d:00", math.floor(hour), (hour % 1) * 60)
            task.wait(CYCLE_SPEED / 240)
        end
    end
end)
""",

"vehicle_spawn": """
-- 🚗 VEHICLE SPAWNER SCRIPT
-- 1. Place your Vehicle model inside ServerStorage
-- 2. Place this Script inside a Part (spawn pad)
-- 3. Change VEHICLE_NAME to your vehicle's name

local part = script.Parent
local ServerStorage = game:GetService("ServerStorage")
local VEHICLE_NAME = "Car" -- ✏️ Change to your vehicle model name
local debounce = false

part.Touched:Connect(function(hit)
    if debounce then return end
    local character = hit.Parent
    local player = game.Players:GetPlayerFromCharacter(character)
    if player then
        debounce = true
        local vehicle = ServerStorage:FindFirstChild(VEHICLE_NAME)
        if vehicle then
            local clone = vehicle:Clone()
            clone.Parent = workspace
            clone:SetPrimaryPartCFrame(part.CFrame + Vector3.new(0, 5, 0))
        end
        task.wait(2)
        debounce = false
    end
end)
""",

"chat_command": """
-- 💬 CHAT COMMAND SYSTEM
-- Place inside ServerScriptService
-- Players type commands in chat to trigger effects

local Players = game:GetService("Players")

local COMMANDS = {
    ["!speed"] = function(player, args)
        local speed = tonumber(args[1]) or 32
        local humanoid = player.Character and player.Character:FindFirstChildOfClass("Humanoid")
        if humanoid then humanoid.WalkSpeed = speed end
        print(player.Name .. " set speed to " .. speed)
    end,
    ["!jump"] = function(player, args)
        local power = tonumber(args[1]) or 100
        local humanoid = player.Character and player.Character:FindFirstChildOfClass("Humanoid")
        if humanoid then humanoid.JumpPower = power end
        print(player.Name .. " set jump to " .. power)
    end,
    ["!reset"] = function(player)
        local humanoid = player.Character and player.Character:FindFirstChildOfClass("Humanoid")
        if humanoid then humanoid.Health = 0 end
    end,
}

Players.PlayerAdded:Connect(function(player)
    player.Chatted:Connect(function(message)
        local parts = message:split(" ")
        local cmd = parts[1]:lower()
        local args = {table.unpack(parts, 2)}
        if COMMANDS[cmd] then
            COMMANDS[cmd](player, args)
        end
    end)
end)
""",

"npc_dialog": """
-- 🗣️ NPC DIALOG SCRIPT
-- Place inside an NPC Model as a Script
-- The NPC will talk when a player gets close

local npc = script.Parent
local Players = game:GetService("Players")

local DIALOG_LINES = {
    "Hello, traveller! Welcome to the game.",
    "Have you explored the map yet?",
    "Watch out for danger ahead!",
}

local function showDialog(player, text)
    local gui = Instance.new("BillboardGui")
    gui.Size = UDim2.new(0, 200, 0, 50)
    gui.StudsOffset = Vector3.new(0, 3, 0)
    gui.Adornee = npc:FindFirstChild("Head") or npc.PrimaryPart
    gui.Parent = npc

    local label = Instance.new("TextLabel")
    label.Size = UDim2.new(1, 0, 1, 0)
    label.BackgroundTransparency = 0.3
    label.BackgroundColor3 = Color3.fromRGB(0,0,0)
    label.TextColor3 = Color3.fromRGB(255,255,255)
    label.TextScaled = true
    label.Text = text
    label.Parent = gui

    task.wait(3)
    gui:Destroy()
end

-- Trigger dialog when player is near
task.spawn(function()
    while true do
        for _, player in ipairs(Players:GetPlayers()) do
            local char = player.Character
            if char then
                local root = char:FindFirstChild("HumanoidRootPart")
                local npcRoot = npc:FindFirstChild("HumanoidRootPart") or npc.PrimaryPart
                if root and npcRoot then
                    local dist = (root.Position - npcRoot.Position).Magnitude
                    if dist < 15 then
                        local line = DIALOG_LINES[math.random(#DIALOG_LINES)]
                        showDialog(player, line)
                        task.wait(5)
                    end
                end
            end
        end
        task.wait(1)
    end
end)
""",

"invisibility": """
-- 👻 INVISIBILITY SCRIPT
-- Place inside a Part as a Script
-- Touch the part to turn invisible for 5 seconds

local part = script.Parent
local DURATION = 5 -- ✏️ Seconds invisible
local debounce = false

local function setTransparency(character, value)
    for _, part in ipairs(character:GetDescendants()) do
        if part:IsA("BasePart") and part.Name ~= "HumanoidRootPart" then
            part.Transparency = value
        end
    end
end

part.Touched:Connect(function(hit)
    if debounce then return end
    local character = hit.Parent
    local humanoid = character:FindFirstChildOfClass("Humanoid")
    if humanoid then
        debounce = true
        setTransparency(character, 1)
        task.wait(DURATION)
        setTransparency(character, 0)
        debounce = false
    end
end)
""",

"forcefield": """
-- 🛡️ FORCE FIELD SCRIPT
-- Place inside a Part as a Script
-- Touch to get a ForceField for 5 seconds

local part = script.Parent
local DURATION = 5 -- ✏️ Seconds of protection
local debounce = false

part.Touched:Connect(function(hit)
    if debounce then return end
    local character = hit.Parent
    local player = game.Players:GetPlayerFromCharacter(character)
    if player then
        debounce = true
        local ff = Instance.new("ForceField")
        ff.Parent = character
        task.wait(DURATION)
        ff:Destroy()
        debounce = false
    end
end)
""",

"music_player": """
-- 🎵 MUSIC PLAYER SCRIPT
-- Place inside ServerScriptService
-- Add your Sound IDs to the PLAYLIST table

local PLAYLIST = {
    "rbxassetid://1234567890",  -- ✏️ Replace with real Sound IDs
    "rbxassetid://0987654321",
}

local sound = Instance.new("Sound")
sound.Parent = workspace
sound.Volume = 0.5

task.spawn(function()
    local index = 1
    while true do
        sound.SoundId = PLAYLIST[index]
        sound:Play()
        repeat task.wait(1) until not sound.IsPlaying
        index = (index % #PLAYLIST) + 1
    end
end)
""",

"datastore": """
-- 💾 DATASTORE (SAVE/LOAD DATA)
-- Place inside ServerScriptService
-- Saves and loads player Cash automatically

local Players = game:GetService("Players")
local DataStoreService = game:GetService("DataStoreService")
local playerData = DataStoreService:GetDataStore("PlayerData_v1")

local function saveData(player)
    local leaderstats = player:FindFirstChild("leaderstats")
    if leaderstats then
        local cash = leaderstats:FindFirstChild("Cash")
        if cash then
            local success, err = pcall(function()
                playerData:SetAsync(tostring(player.UserId), cash.Value)
            end)
            if not success then warn("Save failed: " .. err) end
        end
    end
end

local function loadData(player)
    local leaderstats = Instance.new("Folder")
    leaderstats.Name = "leaderstats"
    leaderstats.Parent = player

    local cash = Instance.new("IntValue")
    cash.Name = "Cash"
    cash.Parent = leaderstats

    local success, data = pcall(function()
        return playerData:GetAsync(tostring(player.UserId))
    end)

    if success and data then
        cash.Value = data
    else
        cash.Value = 0
    end
end

Players.PlayerAdded:Connect(loadData)
Players.PlayerRemoving:Connect(saveData)
game:BindToClose(function()
    for _, player in ipairs(Players:GetPlayers()) do
        saveData(player)
    end
end)
""",

"tween_move": """
-- 🎞️ TWEEN MOVING PLATFORM SCRIPT
-- Place inside a Part as a Script
-- The part will smoothly move back and forth

local TweenService = game:GetService("TweenService")
local part = script.Parent

local MOVE_OFFSET = Vector3.new(20, 0, 0) -- ✏️ Direction & distance
local TWEEN_TIME = 2                        -- ✏️ Seconds per move

local startPos = part.Position
local endPos = startPos + MOVE_OFFSET

local tweenInfo = TweenInfo.new(TWEEN_TIME, Enum.EasingStyle.Sine, Enum.EasingDirection.InOut, -1, true)
local tween = TweenService:Create(part, tweenInfo, {Position = endPos})
tween:Play()
""",

"explosion": """
-- 💥 EXPLOSION SCRIPT
-- Place inside a Part as a Script
-- Touch the part to trigger an explosion

local part = script.Parent
local debounce = false

part.Touched:Connect(function(hit)
    if debounce then return end
    local character = hit.Parent
    local humanoid = character:FindFirstChildOfClass("Humanoid")
    if humanoid then
        debounce = true
        local explosion = Instance.new("Explosion")
        explosion.Position = part.Position
        explosion.BlastRadius = 10   -- ✏️ Radius
        explosion.BlastPressure = 500000
        explosion.Parent = workspace
        task.wait(2)
        debounce = false
    end
end)
""",

"random_teleport": """
-- 🎲 RANDOM TELEPORT SCRIPT
-- Place inside a Part as a Script
-- Teleports the player to a random position

local part = script.Parent
local debounce = false

local SPAWN_AREA = 100 -- ✏️ How far to teleport (studs)

part.Touched:Connect(function(hit)
    if debounce then return end
    local character = hit.Parent
    local humanoid = character:FindFirstChildOfClass("Humanoid")
    if humanoid then
        debounce = true
        local root = character:FindFirstChild("HumanoidRootPart")
        if root then
            local randomX = math.random(-SPAWN_AREA, SPAWN_AREA)
            local randomZ = math.random(-SPAWN_AREA, SPAWN_AREA)
            root.CFrame = CFrame.new(randomX, 10, randomZ)
        end
        task.wait(1)
        debounce = false
    end
end)
""",

"team_system": """
-- 👥 TEAM SYSTEM SCRIPT
-- Place inside ServerScriptService
-- Assigns players to teams when they join

local Teams = game:GetService("Teams")
local Players = game:GetService("Players")

-- Create teams
local function createTeam(name, color)
    local existing = Teams:FindFirstChild(name)
    if existing then return existing end
    local team = Instance.new("Team")
    team.Name = name
    team.TeamColor = color
    team.AutoAssignable = true
    team.Parent = Teams
    return team
end

local redTeam  = createTeam("Red Team",  BrickColor.new("Bright red"))
local blueTeam = createTeam("Blue Team", BrickColor.new("Bright blue"))

-- Balance teams on join
Players.PlayerAdded:Connect(function(player)
    local redCount  = 0
    local blueCount = 0
    for _, p in ipairs(Players:GetPlayers()) do
        if p.Team == redTeam  then redCount  = redCount  + 1 end
        if p.Team == blueTeam then blueCount = blueCount + 1 end
    end
    player.Team = (redCount <= blueCount) and redTeam or blueTeam
    print(player.Name .. " joined " .. player.Team.Name)
end)
""",

}

# ============================================================
# 🧠 AI INTENT DETECTION
# ============================================================

def detect_intent(user_input):
    user_input = user_input.lower().strip()
    best_intent = None
    best_score = 0

    for intent, keywords in INTENT_MAP.items():
        for keyword in keywords:
            if keyword in user_input:
                score = len(keyword)
                if score > best_score:
                    best_score = score
                    best_intent = intent

    return best_intent

# ============================================================
# 📋 HELP MENU
# ============================================================

def print_help():
    print("""
╔══════════════════════════════════════════════════════════╗
║           🎮 ROBLOX SCRIPT AI, WHAT I CAN MAKE          ║
╠══════════════════════════════════════════════════════════╣
║  kill brick         leaderboard        teleport pad      ║
║  speed boost        jump boost         door              ║
║  reset player       gui message        tool giver        ║
║  admin check        shop system        checkpoint        ║
║  countdown timer    day night cycle    vehicle spawner   ║
║  chat commands      npc dialog         invisibility      ║
║  forcefield         music player       datastore         ║
║  tween platform     explosion          random teleport   ║
║  team system                                             ║
╠══════════════════════════════════════════════════════════╣
║  Type 'help' to show this menu  |  Type 'quit' to exit   ║
╚══════════════════════════════════════════════════════════╝
""")

# ============================================================
# 🚀 MAIN LOOP, The AI listens and responds
# ============================================================

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║         🎮 ROBLOX SCRIPT AI ASSISTANT  v2.0              ║
║     Tell me what you want, I'll write the Lua code!     ║
╚══════════════════════════════════════════════════════════╝
""")
    print_help()

    while True:
        try:
            user_input = input("🎮 You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Goodbye! Happy building in Roblox Studio!")
            break

        if not user_input:
            continue

        if user_input.lower() in ["quit", "exit", "bye", "q"]:
            print("👋 Goodbye! Happy building in Roblox Studio!")
            break

        if user_input.lower() in ["help", "list", "menu", "?"]:
            print_help()
            continue

        intent = detect_intent(user_input)

        if intent and intent in SCRIPTS:
            print(f"\n✅ Got it! Here's your Lua script for: {intent.replace('_', ' ').title()}")
            print("=" * 60)
            print(SCRIPTS[intent])
            print("=" * 60)
            print("📋 Copy the code above and paste it into Roblox Studio!\n")
        else:
            print(f"""
❌ Hmm, I'm not sure what script you need.
   Try being more specific, for example:
   → "make a kill brick"
   → "add a leaderboard with cash"
   → "give player a speed boost when they touch a part"

   Type 'help' to see everything I can make!
""")

# ============================================================
if __name__ == "__main__":
    main()
