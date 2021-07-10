-- If LuaRocks is installed, make sure that packages installed through it are
-- found (e.g. lgi). If LuaRocks is not installed, do nothing.
pcall(require, "luarocks.loader")
local gears = require("gears")
local awful = require("awful")
require("awful.autofocus")
local wibox = require("wibox")
local beautiful = require("beautiful")
local naughty = require("naughty")
local menubar = require("menubar")
local hotkeys_popup = require("awful.hotkeys_popup")
require("awful.hotkeys_popup.keys")
require("layouts")
require("errors")
local scratch = require("scratch")
screen_width = awful.screen.focused().geometry.width
screen_height = awful.screen.focused().geometry.height
local sharedtags = require("sharedtags")

-- {{{ Variable definitions
-- Themes define colours, icons, font and wallpapers.
beautiful.init("~/.config/awesome/theme.lua")

-- This is used later as the default terminal and editor to run.
terminal = "st"
editor = "Emacs"
editor_cmd = terminal .. " -e " .. "nvim"
modkey = "Mod4"

-- Menubar configuration
menubar.utils.terminal = terminal -- Set the terminal for applications that require it
mykeyboardlayout = awful.widget.keyboardlayout()
local tags = sharedtags({
    { name = "Α", screen = 1, layout = awful.layout.layouts[1] },
    { name = "Β", screen = 2, layout = awful.layout.layouts[1] },
    { name = "Γ", layout = awful.layout.layouts[1] },
    { name = "Δ", layout = awful.layout.layouts[1] },
    { name = "Ε", layout = awful.layout.layouts[1] },
    { name = "Ζ", layout = awful.layout.layouts[1] },
    { name = "Η", layout = awful.layout.layouts[1] },
    { name = "Θ", layout = awful.layout.layouts[1] },
    { name = "Ι", layout = awful.layout.layouts[1] },
    { layout = awful.layout.layouts[2] },
    { screen = 2, layout = awful.layout.layouts[2] }
})
for i = 1,9 do
    tags[i].useless_gap = 6
end


awful.screen.connect_for_each_screen(function(s)

local my_textclock = wibox.widget {
    format = '%e.%m.%Y, %T',
    refresh = 1,
    opacity = 1,
    widget = wibox.widget.textclock
}

        --awful.tag({"Α", "Β", "Γ", "Δ", "Ε", "Ζ", "Η", "Θ", "Ι"}, s, awful.layout.layouts[1])

    s.mytaglist = awful.widget.taglist {
        screen  = s,
        filter  = awful.widget.taglist.filter.all,
    }

    -- Create a tasklist widget
    s.mytasklist = awful.widget.tasklist {
        screen  = s,
        filter  = awful.widget.tasklist.filter.currenttags,
        style    = {
            shape        = gears.shape.rounded_bar,
            bg_normal = beautiful.bg_normal .. "0",
        },
    }

    -- Create the wibox
    s.wibox_left = awful.wibar({
            screen = s,
            bg = beautiful.bg_normal .. "40",
            width = 200,
            height = 20,
            shape = gears.shape.rounded_bar})

    s.wibox_mid = awful.wibar({
            screen = s,
            position = "right",
            bg = beautiful.bg_normal .. "40",
            width = 700,
            height = 20,
            shape = gears.shape.rounded_bar})

    s.wibox_right = awful.wibar({
            screen = s,
            position = "left",
            bg = beautiful.bg_normal .. "40",
            width = 220,
            height = 20,
            shape = gears.shape.rounded_bar})

    s.wibox_left:setup {
        layout = wibox.layout.fixed.horizontal,
        awful.widget.layoutbox(s),
        s.mytaglist,
    }

    s.wibox_mid:setup {
        layout = wibox.layout.align.horizontal,
        {layout = wibox.layout.fixed.horizontal},
        s.mytasklist,
    }

    s.wibox_right:setup {
            layout = wibox.layout.fixed.horizontal,
            my_textclock,
            wibox.widget {
                style    = {
                    bg_systray = beautiful.bg_systray .. "00",
                    shape = gears.shape.rounded_bar,
                },
                widget = wibox.widget.systray
            },
    }
    awful.placement.top_left(s.wibox_left)
    awful.placement.top(s.wibox_mid)
    awful.placement.top_right(s.wibox_right)
end)
-- }}}

-- {{{ Mouse bindings
-- }}}

-- {{{ Key bindings
globalkeys = gears.table.join(
    awful.key({ modkey,           }, "s",      hotkeys_popup.show_help,
              {description="show help", group="awesome"}),

    awful.key({ modkey,           }, "j",
        function ()
            awful.client.focus.byidx( 1)
        end,
        {description = "focus next by index", group = "client"}
    ),
    awful.key({ modkey,           }, "k",
        function ()
            awful.client.focus.byidx(-1)
        end,
        {description = "focus previous by index", group = "client"}
    ),
    awful.key({ modkey }, "F12", function () scratch.drop("st", "top", "center", 720, 400) end),
    -- Layout manipulation
    awful.key({ modkey, "Shift"   }, "j", function () awful.client.swap.byidx(  1)    end),
    awful.key({ modkey, "Shift"   }, "k", function () awful.client.swap.byidx( -1)    end),
    awful.key({ modkey, "Control" }, "j", function () awful.screen.focus_relative( 1) end),
    awful.key({ modkey, "Control" }, "k", function () awful.screen.focus_relative(-1) end),
    awful.key({ modkey,           }, "u", awful.client.urgent.jumpto,
        {description = "jump to urgent client", group = "client"}),


    awful.key({ modkey,           }, "Tab", function () awful.layout.inc(1) end),

    -- Standard program
    awful.key({ modkey,           }, "q", awesome.restart),
    awful.key({ modkey, "Shift"   }, "q", awesome.quit),

    awful.key({ modkey,           }, "l",     function () awful.tag.incmwfact( 0.05)          end),
    awful.key({ modkey,           }, "h",     function () awful.tag.incmwfact(-0.05)          end)
)

clientkeys = gears.table.join(
    awful.key({ modkey,           }, "f",
        function (c)
            c.fullscreen = not c.fullscreen
            c:raise()
        end,
        {description = "toggle fullscreen", group = "client"}),
    awful.key({ modkey, "Shift"   }, "c",      function (c) c:kill()                         end),
    awful.key({ modkey,           }, "g",  awful.client.floating.toggle                     ),
    awful.key({ modkey, "Control" }, "Return", function (c) c:swap(awful.client.getmaster()) end),
    awful.key({ modkey,           }, "v",      function (c) c:move_to_screen()               end),
    awful.key({ modkey,           }, "t",      function (c) c.ontop = not c.ontop            end)
)

for i = 1, 9 do
    globalkeys = gears.table.join(globalkeys,
        -- View tag only.
        awful.key({ modkey }, "#" .. i + 9,
                  function ()
                        local screen = awful.screen.focused()
                        local tag = tags[i]
                        if tag then
                           sharedtags.viewonly(tag, screen)
                        end
                  end,
                  {description = "view tag #"..i, group = "tag"}),
        -- Toggle tag display.
        awful.key({ modkey, "Control" }, "#" .. i + 9,
                  function ()
                      local screen = awful.screen.focused()
                      local tag = tags[i]
                      if tag then
                         sharedtags.viewtoggle(tag, screen)
                      end
                  end,
                  {description = "toggle tag #" .. i, group = "tag"}),
        -- Move client to tag.
        awful.key({ modkey, "Shift" }, "#" .. i + 9,
                  function ()
                      if client.focus then
                          local tag = tags[i]
                          if tag then
                              client.focus:move_to_tag(tag)
                          end
                     end
                  end,
                  {description = "move focused client to tag #"..i, group = "tag"}),
        -- Toggle tag on focused client.
        awful.key({ modkey, "Control", "Shift" }, "#" .. i + 9,
                  function ()
                      if client.focus then
                          local tag = tags[i]
                          if tag then
                              client.focus:toggle_tag(tag)
                          end
                      end
                  end,
                  {description = "toggle focused client on tag #" .. i, group = "tag"})
    )
end
clientbuttons = gears.table.join(
    awful.button({ }, 1, function (c)
        c:emit_signal("request::activate", "mouse_click", {raise = true})
    end),
    awful.button({ modkey }, 1, function (c)
        c:emit_signal("request::activate", "mouse_click", {raise = true})
        awful.mouse.client.move(c)
    end),
    awful.button({ modkey }, 3, function (c)
        c:emit_signal("request::activate", "mouse_click", {raise = true})
        awful.mouse.client.resize(c)
    end)
)




-- Set keys
root.keys(globalkeys)
-- }}}

-- {{{ Rules
-- Rules to apply to new clients (through the "manage" signal).
awful.rules.rules = {
    -- All clients will match this rule.
    { rule = { },
      properties = { border_width = beautiful.border_width,
                     border_color = beautiful.border_normal,
                     focus = awful.client.focus.filter,
                     raise = true,
                     keys = clientkeys,
                     buttons = clientbuttons,
                     screen = awful.screen.preferred,
                     placement = awful.placement.no_overlap+awful.placement.no_offscreen
     }
    },

    -- Floating clients.
    { rule_any = {
        instance = {
          "DTA",  -- Firefox addon DownThemAll.
          "copyq",  -- Includes session name in class.
          "pinentry",
        },
        class = {
          "Sxiv",
          "Tor Browser", -- Needs a fixed window size to avoid fingerprinting by screen size.
          "xtightvncviewer"},

        -- Note that the name property shown in xprop might be set slightly after creation of the client
        -- and the name shown there might not match defined rules here.
        name = {
          "Event Tester",  -- xev.
        },
        role = {
          "pop-up",       -- e.g. Google Chrome's (detached) Developer Tools.
        }
      }, properties = { floating = true }},

    -- Add titlebars to normal clients and dialogs
    { rule_any = {type = { "normal", "dialog" }
      }, properties = { titlebars_enabled = true }
    },
 {
        rule_any = {
            instance = { "scratch" },
            class = { "scratch" },
            icon_name = { "scratchpad_urxvt" },
        },
        properties = {
            skip_taskbar = false,
            floating = true,
            ontop = false,
            minimized = true,
            sticky = false,
            width = screen_width * 0.7,
            height = screen_height* 0.75
        },
        callback = function (c)
            awful.placement.centered(c,{honor_padding = true, honor_workarea=true})
            gears.timer.delayed_call(function()
                c.urgent = false
            end)
        end
    },
    -- Set Firefox to always map on the tag named "2" on screen 1.
    -- { rule = { class = "Firefox" },
    --   properties = { screen = 1, tag = "2" } },
}
-- }}}

-- {{{ Signals
-- Signal function to execute when a new client appears.
client.connect_signal("manage", function (c)
    -- Set the windows at the slave,
    -- i.e. put it at the end of others instead of setting it master.
    if not awesome.startup then awful.client.setslave(c) end

    if awesome.startup
      and not c.size_hints.user_position
      and not c.size_hints.program_position then
        -- Prevent clients from being unreachable after screen count changes.
        awful.placement.no_offscreen(c)
    end
end)


-- Enable sloppy focus, so that focus follows mouse.
client.connect_signal("mouse::enter", function(c)
    c:emit_signal("request::activate", "mouse_enter", {raise = false})
end)

client.connect_signal("focus", function(c) c.border_color = beautiful.border_focus end)
client.connect_signal("unfocus", function(c) c.border_color = beautiful.border_normal end)
-- }}}
