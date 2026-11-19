# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 496 (printed ٤٩٥)."""

PAGE_NUMBER = 496
PRINTED_PAGE = "٤٩٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «عن توهم كون ما بعدها جملة معطوفة» at the foot of PDF p. 495.
    {"type": "matn",
     "ar": "على الجملة السابقة:",
     "en": "…upon the preceding sentence:"},
    {"type": "matn",
     "ar": "١-(أمر) نحو: «زرني فأكرمك» أي: ليكن منك زيارة فإكرام مني.",
     "en": "1. (A command), as in “zurnī fa-ukrimaka” (visit me, and I will honour you), that is, “let there be a visit from you, and [consequently] honouring from me.”"},
    {"type": "matn",
     "ar": "٢-(أو نهي) نحو: «لا تشتمني فأضربك» أي: لا يكن منك شتم فضرب مني،",
     "en": "2. (Or a prohibition), as in “lā tashtimnī fa-aḍribaka” (do not revile me, lest I strike you), that is, “let there not be reviling from you, and [consequently] striking from me.”"},
    {"type": "matn",
     "ar": "ويندرج فيهما الدعاء[[١]] نحو: «اللهم اغفر لي فأفوز ولا تؤاخذني فأهلك».",
     "en": "Supplication (duʿāʾ) is included under these two, as in “O Allah, forgive me, that I may triumph, and do not take me to task, lest I perish.”"},
    # REVIEW: printed «فأشربها» (feminine pronoun referring to «ماء»); transcribed as printed.
    {"type": "matn",
     "ar": "٣-(أو استفهام) نحو: «هل عندكم ماء فأشربها؟» أي: هل يكون منكم ماء فشرب مني؟",
     "en": "3. (Or a question), as in “hal ʿindakum māʾun fa-ashrabahā?” (Have you any water, that I may drink it?), that is, “will there be water from you, and [consequently] drinking from me?”"},
    {"type": "matn",
     "ar": "٤-(أو نفي) نحو: «ما تأتينا فتحدثنا» أي: ليس منك إتيان فتحديث منا،",
     "en": "4. (Or a negation), as in “mā taʾtīnā fa-tuḥaddithanā” (you do not come to us so as to talk with us), that is, “there is no coming from you, and [consequently] talk with us.”"},
    {"type": "matn",
     "ar": "ويندرج فيه التحضيض نحو: ﴿لولا أنزل إليه ملك فيكون معه نذيرا﴾[[٢]] لاستلزامه نفي فعل، فيندرج[[٣]] في النفي.",
     "en": "Incitement (taḥḍīḍ) is included under it, as in “Why has an angel not been sent down to him, to be a warner with him?”, because it entails the negation of an act, and so it is included under negation."},
    {"type": "matn",
     "ar": "٥-(أو تمن) نحو: «ليت لي مالا فأنفقه» أي: ليت لي ثبوت مال فإنفاق مني،",
     "en": "5. (Or a wish), as in “layta lī mālan fa-unfiqahu” (would that I had wealth, that I might spend it), that is, “would that I had the existence of wealth, and [consequently] spending from me.”"},
    {"type": "matn",
     "ar": "ويدخل فيه[[٤]] ما وقع على صيغة الترجي نحو: ﴿لعلي أبلغ الأسباب أسباب السماوات فأطلع﴾[[٥]] بالنصب على قراءة «حفص».",
     "en": "Included under it is what comes in the form of hope (tarajjī), as in “That I may reach the ways, the ways of the heavens, and look upon…”, with the accusative [fa-aṭṭaliʿa] in the reading of “Ḥafṣ”."},
    {"type": "matn",
     "ar": "٦-(أو عرض[[٦]]) نحو: «ألا تنزل فتصيب خيرا» أي: ألا يكون منك نزول فإصابة خير مني.",
     "en": "6. (Or an offer (ʿarḍ)), as in “a-lā tanzilu fa-tuṣība khayran” (will you not alight, and receive some good?), that is, “will there not be alighting from you, and [consequently] receiving good from me?”"},
    # REVIEW: printed «وما بعدها الفاء» (expected «وما بعد الفاء»); transcribed as printed.
    {"type": "matn",
     "ar": "ففي جملة هذه المواضع معنى السببية مقصود، والفاء تدل عليها، وما بعدها الفاء في تأويل مصدر معطوف على مصدر آخر مفهوم مما قبل الفاء.",
     "en": "In all of these cases the sense of causation is intended and the fāʾ indicates it; and what follows the fāʾ is interpreted as a verbal noun coordinated upon another verbal noun understood from what precedes the fāʾ."},
    {"type": "matn",
     "ar": "وأما نحو:",
     "en": "As for something like:"},
    {"type": "verse",
     "ar": "سأترك منزلي لبني تميم          وألحق بالحجاز فأستريحا",
     "en": "I shall leave my dwelling to the Banū Tamīm / and join the Ḥijāz, and so be at rest,"},
    {"type": "matn",
     "ar": "بدون تقديم أحد الأشياء الستة، فمحمول على ضرورة الشعر.",
     "en": "without one of the six things placed before it, it is to be taken as poetic licence (ḍarūrat al-shiʿr)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: المراد بالأمر والنهي مصطلح النحاة لا مصطلح الأصول.",
     "en": "That is, what is meant by command and prohibition is the grammarians’ technical usage, not that of legal theory (uṣūl)."},
    # REVIEW: printed «اتق الله مرؤ»; the usual form of this example is «اتقى الله امرؤ». Transcribed as printed.
    {"type": "pair",
     "ar": "وعند الكسائي: ما مدلوله الأمر نحو: اتق الله مرؤ وفعل فيثاب عليه، أو اسم فعل نحو: نزال وقرقار،",
     "en": "According to al-Kisāʾī, [it includes] what signifies a command, as in “Let a man fear Allah and act, and he will be rewarded for it”, or a verbal noun of command (ism fiʿl), as in “nazāli” (alight!) and “qarqāri” (rumble!);"},
    {"type": "pair",
     "ar": "أو يكون الأمر فيه مقدرا نحو: الأسد الأسد، فهو جار مجرى الصريح.",
     "en": "or where the command in it is supposed, as in “al-asada al-asada” (the lion, the lion!); for that functions like the explicit [command]."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة الفرقان: ٧.",
     "en": "(Qurʾān, Sūrat al-Furqān 25:7)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لأن المراد بالنفي أعم من أن يكون صريحا أو ضمنا.",
     "en": "Because what is meant by negation is more general than its being explicit or implicit."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لأن المراد ما فيه معنى التمني إما بصيغة أو بغير صيغة.",
     "en": "Because what is meant is whatever carries the sense of a wish, whether with the [proper] form or without it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سورة غافر: ٣٦-٣٧.",
     "en": "(Qurʾān, Sūrat Ghāfir 40:36–37)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "والعرض وإن كان من الاستفهام، لكن لم يبق فيه معنى الاستفهام، وصار معنى آخر برأسه، فلذا لم يدرجه فيه.",
     "en": "The offer, though it derives from the question, no longer retains the sense of a question and has become a separate meaning in its own right; hence he did not include it under it."},
]
