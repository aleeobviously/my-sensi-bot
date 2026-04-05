import telebot
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

# --- SETTINGS ---
TOKEN = '8690581126:AAEUk419U756Q6iqnWL5jgCiRiMdSxHcPf0'
CHANNEL_ID = "@RynoxCheats"
BOT_USERNAME = "RynoxSensi_bot" 
BOT_URL = f"https://t.me/{BOT_USERNAME}"

bot = telebot.TeleBot(TOKEN, threaded=True, num_threads=30)

user_data = {}

# --- TRANSLATIONS (Exact Icons from your image) ---
STRINGS = {
    'en': {
        'welcome': "👋 **𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗥𝗬𝗡𝗢𝗫 𝗦𝗘𝗡𝗦𝗜 𝗔𝗜!**\n\nPlease join our channel to unlock the premium settings.",
        'select_hz': "🔥 **𝗥𝗬𝗡𝗢𝗫 𝗦𝗘𝗡𝗦𝗜 𝗔𝗜**\n\nSelect your **Device Refresh Rate**:",
        'analyzing': "⏳ **𝗔𝗜 𝗔𝗡𝗔𝗟𝗬𝗭𝗜𝗡𝗚 𝗦𝗘𝗡𝗦𝗢𝗥𝗦...**",
        'choice': "Which settings do you want to generate?",
        'share': "🚀 𝗦𝗛𝗔𝗥𝗘 𝗕𝗢𝗧",
        'back': "⬅️ 𝗕𝗔𝗖𝗞",
        'lens_head': "🎯 **LENS TAB**",
        'gyro_head': "🌀 **GYROSCOPE TAB**",
        'cam_sens': "🎯 **𝗖𝗔𝗠𝗘𝗥𝗔 𝗦𝗘𝗡𝗦𝗜𝗧𝗜𝗩𝗜𝗧𝗬**",
        'ads_sens': "🎯 **𝗔𝗗𝗦 𝗦𝗘𝗡𝗦𝗜𝗧𝗜𝗩𝗜𝗧𝗬**",
        'free_look': "🎯 **𝐅𝐑𝐄𝐄 𝐋𝐎𝐎𝐊 𝐂𝐀𝐌𝐄𝐑𝐀**",
        'gyro_sens': "🌀 **𝗚𝗬𝗥𝗢𝗦𝗖𝗢𝗣𝗘 𝗦𝗘𝗡𝗦𝗜𝗧𝗜𝗩𝗜𝗧𝗬**",
        'ads_gyro': "🌀 **𝗔𝗗𝗦 𝗚𝗬𝗥𝗢𝗦𝗖𝗢𝗣𝗘**",
        'share_text': "Get%20the%20best%20AI%20Sensitivity%20Settings%20here!%20🔥"
    },
    'ur': {
        'welcome': "👋 **𝗥𝗬𝗡𝗢𝗫 𝗦𝗘𝗡𝗦𝗜 𝗔𝗜 میں خوش آمدید!**",
        'select_hz': "🔥 **𝗥𝗬𝗡𝗢𝗫 𝗦𝗘𝗡𝗦𝗜 𝗔𝗜**\n\nاپنے ڈیوائس کی ریفریش ریٹ منتخب کریں:",
        'analyzing': "⏳ **ای آئی سینسرز کا جائزہ لے رہا ہے...**",
        'choice': "آپ کون سی سیٹنگز دیکھنا چاہتے ہیں؟",
        'share': "🚀 𝗦𝗛𝗔𝗥𝗘 𝗕𝗢𝗧",
        'back': "⬅️ واپسی",
        'lens_head': "🎯 **LENS TAB**",
        'gyro_head': "🌀 **GYROSCOPE TAB**",
        'cam_sens': "🎯 **کیمرہ حساسیت**",
        'ads_sens': "🎯 **ADS حساسیت**",
        'free_look': "🎯 **فری لک کیمرہ**",
        'gyro_sens': "🌀 **جائروسکوپ حساسیت**",
        'ads_gyro': "🌀 **ADS جائروسکوپ**"
    },
    'hi': {
        'welcome': "👋 **𝗥𝗬𝗡𝗢𝗫 𝗦𝗘𝗡𝗦𝗜 𝗔𝗜 में आपका स्वागत है!**",
        'select_hz': "🔥 **𝗥𝗬𝗡𝗢𝗫 𝗦𝗘𝗡𝗦𝗜 𝗔𝗜**\n\nअपने डिवाइस की रिफ्रेश रेट चुनें:",
        'analyzing': "⏳ **एआई विश्लेषण कर रहा है...**",
        'choice': "आप कौन सी सेटिंग्स देखना चाहते हैं?",
        'share': "🚀 𝗦𝗛𝗔𝗥𝗘 𝗕𝗢𝗧",
        'back': "⬅️ वापस",
        'lens_head': "🎯 **LENS TAB**",
        'gyro_head': "🌀 **GYROSCOPE TAB**",
        'cam_sens': "🎯 **कैमरा संवेदनशीलता**",
        'ads_sens': "🎯 **ADS संवेदनशीलता**",
        'free_look': "🎯 **फ्री लुक कैमरा**",
        'gyro_sens': "🌀 **जाइरोस्कोप संवेदनशीलता**",
        'ads_gyro': "🌀 **ADS जाइरोस्कोप**"
    },
    'ar': {
        'welcome': "👋 **أهلاً بك في 𝗥𝗬𝗡𝗢𝗫 𝗦𝗘𝗡𝗦𝗜 𝗔𝗜!**",
        'select_hz': "🔥 **𝗥𝗬𝗡𝗢𝗫 𝗦𝗘𝗡𝗦𝗜 𝗔𝗜**\n\nاختر معدل تحديث جهازك:",
        'analyzing': "⏳ **الذكاء الاصطناعي يحلل...**",
        'choice': "ما هي الإعدادات التي تريدها؟",
        'share': "🚀 𝗦𝗛𝗔𝗥𝗘 𝗕𝗢𝗧",
        'back': "⬅️ عودة",
        'lens_head': "🎯 **LENS TAB**",
        'gyro_head': "🌀 **GYROSCOPE TAB**",
        'cam_sens': "🎯 **حساسية الكاميرا**",
        'ads_sens': "🎯 **حساسية ADS**",
        'free_look': "🎯 **كاميرا النظرة الحرة**",
        'gyro_sens': "🌀 **حساسية الجيروسكوب**",
        'ads_gyro': "🌀 **جيروسكوب ADS**"
    }
}

# --- AI CALCULATOR ---
def calc(val, hz):
    if hz == "90": return int(val * 1.1)
    if hz == "120": return int(val * 1.2)
    return val

# --- KEYBOARDS ---
def lang_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(InlineKeyboardButton("🇺🇸 English", callback_data="lang_en"),
           InlineKeyboardButton("🇵🇰 Urdu", callback_data="lang_ur"),
           InlineKeyboardButton("🇮🇳 Hindi", callback_data="lang_hi"),
           InlineKeyboardButton("🇸🇦 Arabic", callback_data="lang_ar"))
    return kb

def join_kb(lang):
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(InlineKeyboardButton("📢 𝗝𝗢𝗜𝗡 𝗖𝗛𝗔𝗡𝗡𝗘𝗟", url=f"https://t.me/{CHANNEL_ID.replace('@','')}"))
    kb.add(InlineKeyboardButton("✅ 𝗩𝗘𝗥𝗜𝗙𝗬 𝗝𝗢𝗜𝗡", callback_data="check_verified"))
    return kb

def hz_kb(lang):
    kb = InlineKeyboardMarkup(row_width=3)
    kb.add(InlineKeyboardButton("60 Hz", callback_data="sethz_60"),
           InlineKeyboardButton("90 Hz", callback_data="sethz_90"),
           InlineKeyboardButton("120 Hz+", callback_data="sethz_120"))
    kb.add(InlineKeyboardButton(STRINGS.get(lang, STRINGS['en'])['back'], callback_data="start_over"))
    return kb

def choice_kb(lang, hz):
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(InlineKeyboardButton(STRINGS.get(lang, STRINGS['en'])['lens_head'], callback_data="show_lens"),
           InlineKeyboardButton(STRINGS.get(lang, STRINGS['en'])['gyro_head'], callback_data="show_gyro"))
    kb.add(InlineKeyboardButton(STRINGS.get(lang, STRINGS['en'])['back'], callback_data="check_verified"),
           InlineKeyboardButton(STRINGS.get(lang, STRINGS['en'])['share'], url=f"https://t.me/share/url?url={BOT_URL}"))
    return kb

# --- HELPERS ---
def is_member(user_id):
    try:
        status = bot.get_chat_member(CHANNEL_ID, user_id).status
        return status in ['member', 'administrator', 'creator']
    except: return False

def get_final_text(choice, hz, lang):
    s = STRINGS.get(lang, STRINGS['en'])
    h = str(hz)
    if choice == "lens":
        content = f"""══════════════════
{s['cam_sens']}

Camera Sensitivity
• TPP No Scope: {calc(120, h)}%
• FPP No Scope: {calc(120, h)}%
• Red Dot / Holo: {calc(60, h)}%
• 2x Scope: {calc(35, h)}%
• 3x Scope: {calc(27, h)}%
• 4x Scope: {calc(19, h)}%
• 6x Scope: {calc(12, h)}%
• 8x Scope: {calc(10, h)}%

══════════════════
{s['ads_sens']}

TPP No Scope: {calc(100, h)}%
FPP No Scope: {calc(100, h)}%
Red Dot / Holo: {calc(80, h)}%
2x Scope: {calc(60, h)}%

══════════════════
{s['free_look']}

TPP (Character): {calc(90, h)}%
Parachuting: {calc(100, h)}%"""
    else:
        content = f"""══════════════════
{s['gyro_sens']}

• TPP No Scope: {calc(350, h)}%
• FPP No Scope: {calc(350, h)}%
• Red Dot / Holo: {calc(300, h)}%
• 2x Scope: {calc(300, h)}%
• 3x Scope: {calc(250, h)}%"""

    return f"🔥 **𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗦𝗘𝗡𝗦𝗜𝗧𝗜𝗩𝗜𝗧𝗬** 🔥\n⚙️ Device Mode: {hz}Hz | AI Optimized\n\n{content}\n\n══════════════════\n👤 Owner: @iamRynox\n📢 Channel: @RynoxCheats"

# --- HANDLERS ---
@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "🌐 **𝗦𝗲𝗹𝗲𝗰𝘁 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲**", reply_markup=lang_kb(), parse_mode='Markdown')

@bot.callback_query_handler(func=lambda c: True)
def handle_cb(c):
    uid = c.message.chat.id
    if uid not in user_data: user_data[uid] = {'lang': 'en'}
    lang = user_data[uid]['lang']
    
    if c.data == "start_over":
        bot.edit_message_text("🌐 **𝗦𝗲𝗹𝗲𝗰𝘁 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲**", uid, c.message.message_id, reply_markup=lang_kb(), parse_mode='Markdown')
    elif "lang_" in c.data:
        lang = c.data.replace("lang_", "")
        user_data[uid]['lang'] = lang
        if not is_member(uid):
            bot.edit_message_text(STRINGS.get(lang, STRINGS['en'])['welcome'], uid, c.message.message_id, reply_markup=join_kb(lang), parse_mode='Markdown')
        else:
            bot.edit_message_text(STRINGS.get(lang, STRINGS['en'])['select_hz'], uid, c.message.message_id, reply_markup=hz_kb(lang), parse_mode='Markdown')
    elif c.data == "check_verified":
        if is_member(uid):
            bot.edit_message_text(STRINGS.get(lang, STRINGS['en'])['select_hz'], uid, c.message.message_id, reply_markup=hz_kb(lang), parse_mode='Markdown')
        else:
            bot.answer_callback_query(c.id, "⚠️ JOIN @RynoxCheats FIRST!", show_alert=True)
    elif "sethz_" in c.data:
        hz = c.data.replace("sethz_", "")
        user_data[uid]['hz'] = hz
        bot.edit_message_text(f"⚙️ **𝗠𝗼𝗱𝗲:** {hz}Hz Selected\n\n{STRINGS.get(lang, STRINGS['en'])['choice']}", uid, c.message.message_id, reply_markup=choice_kb(lang, hz), parse_mode='Markdown')
    elif "show_" in c.data:
        choice = c.data.replace("show_", "")
        hz = user_data[uid].get('hz', '60')
        bot.edit_message_text(f"{STRINGS.get(lang, STRINGS['en'])['analyzing']}", uid, c.message.message_id, parse_mode='Markdown')
        time.sleep(0.7)
        final_kb = InlineKeyboardMarkup().add(InlineKeyboardButton(STRINGS.get(lang, STRINGS['en'])['back'], callback_data=f"sethz_{hz}"),
                                             InlineKeyboardButton(STRINGS.get(lang, STRINGS['en'])['share'], url=f"https://t.me/share/url?url={BOT_URL}"))
        bot.edit_message_text(get_final_text(choice, hz, lang), uid, c.message.message_id, reply_markup=final_kb, parse_mode='Markdown')

if __name__ == "__main__":
    bot.infinity_polling()
