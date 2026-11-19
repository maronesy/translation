# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 503 (printed ٥٠٢)."""

PAGE_NUMBER = 503
PRINTED_PAGE = "٥٠٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # PDF p. 502 ends with a complete sentence («لوجوب دخول الفاء عليه.»); a new lemma begins here.
    {"type": "matn",
     "ar": "(وإن كان) أي: الجزاء (مضارعا مثبتا أو منفيا ب«لا») احتراز عما إذا كان منفيا ب«لم»، فإنه مندرج فيما سبق؛ لكونه ماضيا معنى،",
     "en": "(And if it), that is, the requital, (is a muḍāriʿ, affirmative or negated by “lā”): this excludes the case where it is negated by “lam”, for that falls under what preceded, since it is a past in meaning,"},
    {"type": "matn",
     "ar": "أو ب«لن» حيث يجب فيه الفاء، لعدم تأثير أداة الشرط فيه معنى",
     "en": "or by “lan”, where the fāʾ is obligatory, since the particle of condition has no effect on it in meaning;"},
    {"type": "matn",
     "ar": "(فالوجهان) الإتيان بالفاء وتركها؛",
     "en": "(then both treatments) [are allowed]: bringing the fāʾ and leaving it out;"},
    {"type": "matn",
     "ar": "لأن أداة الشرط لم تؤثر في تغيير معناه كما تؤثر في الماضي، فيؤتى بالفاء،",
     "en": "because the particle of condition has not effected a change in its meaning as it does in the past, so the fāʾ is brought;"},
    {"type": "matn",
     "ar": "وأثرت في تغيير المعنى بحيث خلصت لمعنى الاستقبال[[١]]، فيترك الفاء، لوجود التأثير فيه من وجه وإن لم يكن قويا",
     "en": "and it has effected a change in the meaning in that it has made it purely future, so the fāʾ is left out, because there is an effect upon it in one respect, even if not a strong one;"},
    {"type": "matn",
     "ar": "نحو قوله تعالى: ﴿وإن يكن منكم ألف يغلبوا ألفين﴾[[٢]]، ﴿ومن عاد فينتقم الله منه﴾[[٣]]",
     "en": "as in His words, the Exalted, “And if there are among you a thousand, they will overcome two thousand” (Qurʾān, Sūrat al-Anfāl 8:66), and “And whoever returns, Allah will take retribution on him” (Qurʾān, Sūrat al-Māʾida 5:95)."},
    {"type": "matn",
     "ar": "(وإلا) أي: وإن لم يكن الجزاء الماضي أو المضارع المذكورين[[٤]] (فالفاء) لازمة فيه؛",
     "en": "(Otherwise), that is, if the requital is not the past or the muḍāriʿ mentioned, (the fāʾ) is required in it;"},
    {"type": "matn",
     "ar": "لأن الجزاء حينئذ إما ماض ب«قد» لفظا كما تقول: «إن أكرمتني اليوم فقد أكرمتك أمس»",
     "en": "because the requital is then either a past with “qad” in wording, as you say “in akramtanī al-yawma fa-qad akramtuka amsi” (if you honour me today, then I honoured you yesterday),"},
    {"type": "matn",
     "ar": "أو تقديرا كما تقول: «إن أكرمتني اليوم فأكرمتك أمس» بتقدير: فقد أكرمتك،",
     "en": "or by supposition, as you say “in akramtanī al-yawma fa-akramtuka amsi”, with “fa-qad akramtuka” supposed;"},
    {"type": "matn",
     "ar": "وعلى كلا التقدير لا تأثير لحرف الشرط في الماضي، فاحتاج إلى رابطة الفاء،",
     "en": "and on either supposition the particle of condition has no effect on the past, so it needs the connective fāʾ;"},
    # REVIEW: printed «وعلى كلا التقدير» (singular after «كلا»; one would expect «التقديرين»); transcribed as printed.
    {"type": "matn",
     "ar": "وإما جملة اسمية أو أمر أو نهي أو دعاء أو استفهام أو مضارع منفي ب«ما أو لم أو لن» إلى غير ذلك كالتمني والعرض،",
     "en": "or else it is a nominal sentence, or a command, a prohibition, a supplication, a question, or a muḍāriʿ negated by “mā”, “lam” or “lan”, and so on, such as wishing and proposal;"},
    {"type": "matn",
     "ar": "وفي جميع هذه المواضع لا تأثير لحرف الشرط في الجزاء، فاحتاج إلى الفاء.",
     "en": "and in all these places the particle of condition has no effect on the requital, so it needs the fāʾ."},
    {"type": "matn",
     "ar": "(ويجيء «إذا») التي للمفاجأة (مع الجملة الاسمية) التي وقعت جزاء (موضع الفاء)؛",
     "en": "(And “idhā”), the one of surprise (mufājaʾa), (comes with the nominal sentence) that occurs as a requital (in place of the fāʾ),"},
    {"type": "matn",
     "ar": "لأن معناها قريب من معنى الفاء؛ لأنها تنبيء عن حدوث أمر بعد أمر، ففيها معنى الفاء التعقيبية، ولكن الفاء أكثر،",
     "en": "because its meaning is close to the meaning of the fāʾ: it announces the occurrence of one thing after another, so it carries the sense of the fāʾ of immediate sequence (taʿqīb); but the fāʾ is more frequent."},
    {"type": "matn",
     "ar": "وإنما اشترط اسمية الجملة الجزائية لاختصاصها بها؛",
     "en": "He made it a condition that the requital sentence be nominal only because [this idhā] is restricted to it;"},
    {"type": "matn",
     "ar": "لأن «إذا» الشرطية مختصة بالفعلية، فاختصت هذه بالجملة الاسمية فرقا بينهما،",
     "en": "for the conditional “idhā” is restricted to the verbal [sentence], so this one was restricted to the nominal sentence, to distinguish between the two,"},
    {"type": "matn",
     "ar": "كقوله تعالى: ﴿وإن تصبهم سيئة بما قدمت أيديهم إذا هم يقنطون﴾[[٥]] أي: فهم يقنطون.",
     "en": "as in His words, the Exalted, “And if an evil afflicts them for what their hands have put forth, at once they despair” (Qurʾān, Sūrat al-Rūm 30:36), that is, “fa-hum yaqnaṭūn” (then they despair)."},
    {"type": "matn",
     "ar": "(و«إن») التي ينجزم بها المضارع حال كونها (مقدرة) وإنما كانت مقدرة:",
     "en": "(And “in”), by which the muḍāriʿ is put in the jussive while it is (supposed [and unexpressed]); it is supposed only…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لأن المضارع المثبت والمنفي بلا كان محتملا للحال والاستقبال قبل دخول الأداة.",
     "en": "Because the muḍāriʿ, affirmative or negated by lā, admitted both the present and the future before the particle entered."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة الأنفال: ٦٦.",
     "en": "Qurʾān, Sūrat al-Anfāl 8:66."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة المائدة: ٩٥.",
     "en": "Qurʾān, Sūrat al-Māʾida 5:95."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: الماضي بغير قد، ونحوه من الحروف المحققة للماضي لفظا أو معنى، أو المضارع المجرد عن دخول شيء من الحروف مثبتا أو منفيا ب«لا».",
     "en": "That is, the past without qad and similar particles that make the past realized, in wording or in meaning; or the muḍāriʿ free of any particle entering upon it, affirmative or negated by “lā”."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سورة الروم: ٣٦.",
     "en": "Qurʾān, Sūrat al-Rūm 30:36."},
]
