--- Theme by @xStormyy on GitHub
-- Original Color Scheme: https://github.com/BeardedBear/bearded-theme/blob/master/themes/bearded-theme-vivid-black.json


local style = require "core.style"
local common = require "core.common"


--[[
    #////////////////////////////#
                Editor
    #////////////////////////////#
]]--
style.background = { common.color "#050e14" } -- editor
style.syntax["normal"] = { common.color "#c0f0ff" } -- editor text

style.syntax["symbol"] = { common.color "#c0f0ff" }  -- symbols
style.syntax["comment"] = { common.color "#555555" } -- comments
style.syntax["keyword"] = { common.color "#00c0ff" }  -- keywords like function, local, if, end, in lua
style.syntax["keyword2"] = { common.color "#da598c" } -- types
style.syntax["keyword3"] = { common.color "#70ffac" } -- absolutely no idea
style.syntax["number"] = { common.color "#f801e8" } -- numbers
style.syntax["literal"] = { common.color "#ffc47f" } -- literals
style.syntax["string"] = { common.color "#5e3ed9" } -- strings
style.syntax["operator"] = { common.color "#5ab738" } -- operators
style.syntax["function"] = { common.color "#e924f7" }  -- functions

style.caret = { common.color "#ffc47f" } -- caret

style.line_highlight = { common.color "#361336" } -- editor line highlighting
style.selection = { common.color "#392684" } -- editor selection

style.guide = { common.color "#55555530" } -- indentation guide
style.guide_highlighting = { common.color "#555555bb" } -- indentation guide

style.lint = {} -- Lint+
style.lint.info = { common.color "#007ead" } -- Lint+ info
style.lint.hint = { common.color "#42DD76" } -- Lint+ hint
style.lint.warning = { common.color "#FFB638" } -- Lint+ warning
style.lint.error = { common.color "#D62C2C" } -- Lint+ error

--[[
    #////////////////////////////#
           User Interface
    #////////////////////////////#
]]--
style.background2 = { common.color "#0f0f11" } -- sidebar
style.background3 = { common.color "#0f0f11" } -- status bar
style.text = { common.color "#afafafCC" } -- user interface text

style.accent = style.caret -- accent color
style.divider = { common.color "#00c7ff" } -- borders

style.line_number = { common.color "#55555590" } -- inactive
style.line_number2 = { common.color "#555555" } -- active
