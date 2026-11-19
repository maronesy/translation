# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 502 (printed ٥٠١)."""

PAGE_NUMBER = 502
PRINTED_PAGE = "٥٠١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فالمراد بجعلها الشيء» at the foot of PDF p. 501 (mid-sentence).
    {"type": "matn",
     "ar": "سببا أن المتكلم اعتبر سببية شيء لشيء، بل ملزومية شيء لشيء، وجعل كلم المجازاة دالة عليها،",
     "en": "…a cause is that the speaker regards one thing as the cause of another, or rather as entailing another, and makes the words of requital indicate this;"},
    {"type": "matn",
     "ar": "ولا يلزم أن يكون الفعل الأول سببا حقيقيا للثاني لا خارجا ولا ذهنا،",
     "en": "and it is not necessary that the first verb be a real cause of the second, neither in external reality nor in the mind;"},
    {"type": "matn",
     "ar": "بل ينبغي أن يعتبر المتكلم بينهما نسبة يصح بها أن يوردهما في صورة السبب والمسبب، بل الملزوم واللازم،",
     "en": "rather, the speaker must regard between them a relation by which it is valid for him to present them in the form of cause and effect, or rather of entailer and entailed,"},
    {"type": "matn",
     "ar": "كقولك: «إن تشتمني أكرمك»، فالشتم ليس سببا حقيقيا للإكرام، والإكرام مسببا حقيقيا له لا ذهنا ولا خارجا،",
     "en": "as in your saying “in tashtimnī ukrimka” (if you revile me, I will honour you): reviling is not a real cause of honouring, nor is honouring a real effect of it, neither in the mind nor in external reality;"},
    {"type": "matn",
     "ar": "لكن المتكلم اعتبر تلك النسبة بينهما إظهارا لمكارم الأخلاق،",
     "en": "but the speaker regarded that relation between them in order to display noble character;"},
    {"type": "matn",
     "ar": "يعني: أنه منها بمكان يصير الشتم الذي هو سبب الإهانة عند الناس سبب الإكرام عنده.",
     "en": "he means that he possesses such noble character that reviling, which among people is the cause of humiliation, becomes for him the cause of honouring."},
    {"type": "matn",
     "ar": "(ويسميان) أي: هذان الفعلان أو لهما (شرطا)؛ لأنه شرط لتحقق الثاني (و) ثانيهما (جزاء) من حيث إنه يبتني على الأول ابتناء الجزاء على الفعل.",
     "en": "(And they are called), that is, these two verbs, the first of them (a condition (sharṭ)), because it is a condition for the realization of the second, (and) the second of them (a requital (jazāʾ)), in that it is built upon the first as a requital is built upon the deed."},
    {"type": "matn",
     "ar": "(فإن كانا) أي: الشرط والجزاء (مضارعين) نحو: «إن تزرني أزرك» (أو الأول) فقط (مضارعا) نحو: «إن تزرني فقد زرتك»",
     "en": "(So if they), that is, the condition and the requital, (are both muḍāriʿ), as in “in tazurnī azurka” (if you visit me, I will visit you), (or the first) only (is a muḍāriʿ), as in “in tazurnī fa-qad zurtuka” (if you visit me, then I have visited you),"},
    {"type": "matn",
     "ar": "(فالجزم) واجب في المضارع، لدخول الجازم، وهو «إن» أو ما يتضمنها مع صلاحية المحل.",
     "en": "(then the jussive) is obligatory in the muḍāriʿ, because the jussive-governing word has entered, namely “in” or what implicitly contains it, together with the position’s being fit [for it]."},
    {"type": "matn",
     "ar": "(وإن كان الثاني) مضارعا (فالوجهان) أي: ففيه الوجهان:",
     "en": "(And if the second) [only] is a muḍāriʿ, (then both treatments), that is, in it both treatments are allowed:"},
    {"type": "matn",
     "ar": "الجزم لتعلقه بالجازم، وهو أداة الشرط، والرفع لضعف التعلق لحيلولة الماضي والفصل بغير المعمول نحو: «إن أتاني زيد آته أو آتيه».",
     "en": "the jussive, because of its connection with the jussive-governing word, namely the particle of condition; and the nominative, because the connection is weakened by the past verb intervening and by the separation by something not governed [by it], as in “in atānī Zaydun ātihi” or “ātīhi” (if Zayd comes to me, I will come to him)."},
    {"type": "matn",
     "ar": "(وإذا كان الجزاء ماضيا بغير «قد» لفظا) تفصيل للماضي نحو: «إن خرجت خرجت» (أو معنى) نحو: «إن خرجت لم أخرج».",
     "en": "(And when the requital is a past without “qad”, in wording), a specification of the past, as in “in kharajta kharajtu” (if you go out, I go out), (or in meaning), as in “in kharajta lam akhruj” (if you go out, I do not go out);"},
    {"type": "matn",
     "ar": "ويحتمل أن يكون تفصيلا ل«قد» أي: لم يقترن ب«قد» سواء كان «قد» ملفوظا كقوله تعالى: ﴿إن يسرق فقد سرق أخ له من قبل﴾[[١]]",
     "en": "it may also be a specification of “qad”, that is, it is not joined to “qad”, whether “qad” is pronounced, as in His words, the Exalted, “If he steals, then a brother of his stole before” (Qurʾān, Sūrat Yūsuf 12:77),"},
    {"type": "matn",
     "ar": "أو معنويا كقوله تعالى: ﴿إن كان قميصه قد من قبل فصدقت﴾[[٢]] أي: فقد صدقت",
     "en": "or implied in meaning, as in His words, the Exalted, “If his shirt is torn from the front, then she has told the truth” (Qurʾān, Sūrat Yūsuf 12:26), that is, “fa-qad ṣadaqat”;"},
    {"type": "matn",
     "ar": "(لم يجز الفاء في الجزاء) لتحقق تأثير حرف الشرط فيه لقلب معناه إلى الاستقبال، فاستغنوا فيه عن الرابطة",
     "en": "(the fāʾ is not permitted in the requital), because the effect of the particle of condition upon it is realized, in turning its meaning to the future; so they dispensed in it with the connective,"},
    {"type": "matn",
     "ar": "كقولك: «إن أكرمتني أكرمتك»، و«إن أكرمتني لم أكرمك»،",
     "en": "as in your saying “in akramtanī akramtuka” (if you honour me, I honour you) and “in akramtanī lam ukrimka” (if you honour me, I do not honour you)."},
    {"type": "matn",
     "ar": "وإنما قال: «بغير قد»؛ ليخرج عنه الماضي المحقق الذي لا يستقيم أن يكون للشرط تأثير فيه",
     "en": "He said “without qad” only in order to exclude from it the realized past, upon which the condition cannot properly have an effect,"},
    {"type": "matn",
     "ar": "كقولك: «إن أكرمتني اليوم فقد أكرمتك أمس» لوجوب دخول الفاء عليه.",
     "en": "as in your saying “in akramtanī al-yawma fa-qad akramtuka amsi” (if you honour me today, then I honoured you yesterday), since the fāʾ must enter upon it."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة يوسف: ٧٧.",
     "en": "Qurʾān, Sūrat Yūsuf 12:77."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة يوسف: ٢٦.",
     "en": "Qurʾān, Sūrat Yūsuf 12:26."},
]
