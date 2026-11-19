# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 484 (printed ٤٨٣)."""

PAGE_NUMBER = 484
PRINTED_PAGE = "٤٨٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… الماضي مبني على» at the foot of PDF p. 483 (mid-sentence).
    {"type": "matn",
     "ar": "الفتح لفظا، نحو: «ضرب»، أو تقديرا[[١]] نحو: «رمى».",
     "en": "…the fatḥa, either overtly, as in “ḍaraba”, or by implication, as in “ramā”."},
    {"type": "matn",
     "ar": "وأما البناء[[٢]] على الحركة دون السكون الذي هو الأصل في المبني، فلمشابهته المضارع في وقوعه[[٣]] موقع الاسم،",
     "en": "As for its being indeclinable on a vowel rather than on quiescence (sukūn), which is the default in the indeclinable, that is because it resembles the imperfect in occurring in the position of the noun,"},
    {"type": "matn",
     "ar": "نحو: «زيد ضرب» في موقعه «زيد ضارب»، وشرطا وجزاء[[٤]] تقول: «إن ضربتني ضربتك» في موقع «إن تضربني أضربك».",
     "en": "as in “Zayd ḍaraba” in the position of “Zayd ḍārib”, and as condition and apodosis: you say “in ḍarabtanī ḍarabtuka” in the position of “in taḍribnī aḍribka” (if you strike me, I will strike you)."},
    {"type": "matn",
     "ar": "وأما الفتح فلكونه أخف الحركات.",
     "en": "As for the fatḥa, that is because it is the lightest of the vowels."},
    {"type": "matn",
     "ar": "(مع غير الضمير[[٥]] المرفوع المتحرك) فإنه مبني على السكون معه، نحو: «ضربن إلى ضربنا»",
     "en": "(With other than the voweled nominative pronoun), for with it [the past] is indeclinable on quiescence, as in “ḍarabna” through “ḍarabnā”,"},
    {"type": "matn",
     "ar": "كراهة اجتماع[[٦]] أربع حركات فيما هو كالكلمة الواحدة، لشدة اتصال الفاعل[[٧]] بفعله.",
     "en": "from dislike of four consecutive vowels in what is like a single word, because of the close connection of the agent with its verb."},
    {"type": "matn",
     "ar": "وإنما قيد الضمير المرفوع بالمتحرك احترازا عن مثل[[٨]]: «ضربا»، فإنه أيضا مبني على الفتح.",
     "en": "He qualified the nominative pronoun as voweled only as a precaution against the like of “ḍarabā”, for that too is indeclinable on the fatḥa."},
    {"type": "matn",
     "ar": "(و) مع غير (الواو) فإنه يضم معها لمجانستها لفظا كـ«ضربوا» أو تقديرا كـ«رموا».",
     "en": "(And) with other than (the wāw), for with it it takes the ḍamma because of its affinity with it, overtly as in “ḍarabū”, or by implication as in “ramaw”."},

    {"type": "section", "ar": "[الفعل المضارع]",
     "en": "The Imperfect Verb (al-Muḍāriʿ)"},

    {"type": "matn",
     "ar": "(المضارع ما أشبه) أي: فعل أشبه (الاسم بأحد حروف «نأيت») أي: حال",
     "en": "(The imperfect is what resembles), that is, a verb that resembles, (the noun through one of the letters of “naʾaytu”), that is, while…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فإنه يمكنه تقدير الفتحة في آخر \"رمى\" وإن لم تظهر للتعذر،",
     "en": "For the fatḥa can be implied at the end of “ramā”, even though it does not appear because of impossibility (taʿadhdhur),"},
    {"type": "pair",
     "ar": "بخلاف \"ضربن وضربوا\"، فإنه لا يمكن تقدير الفتحة على ما قبل النون والواو، فلذا كانا مبنيين على السكون والضم.",
     "en": "unlike “ḍarabna” and “ḍarabū”, for the fatḥa cannot be implied on what precedes the nūn and the wāw; that is why they are indeclinable on quiescence and on the ḍamma."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فلعدم اعتوار البناء عليه.",
     "en": "[As for indeclinability itself,] it is because no succession [of inflections] befalls it."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: لوقوعه؛ لأن وقوع الماضي موقع الاسم ليس وجه المشابهة.",
     "en": "That is, [it resembles it] because of its occurring; for the past’s occurring in the noun’s position is not the point of resemblance."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "عطف على قوله: موقع أو وقوعه بتقدير وقوعه.",
     "en": "Coordinated with his word “the position”, or with “its occurring”, with “its occurring” understood."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سواء لم يكن معه ضمير أصلا نحو: \"ضرب زيد\"، أو يكون معه ضمير منصوب نحو: ضربك أو مرفوع ساكن نحو: ضربا.",
     "en": "Whether there is no pronoun with it at all, as in “ḍaraba Zayd”, or there is an accusative pronoun with it, as in “ḍarabaka”, or a quiescent nominative one, as in “ḍarabā”."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فلذا قالوا: أصل علبط وهدبد: علابط وهدابد.",
     "en": "That is why they said that the origin of “ʿulabiṭ” and “hudabid” is “ʿulābiṭ” and “hudābid”."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: الضمير بفعله لكونه متصلا لفظا ومعنى بخلاف نحو حركة وتركة، فإن اتصال التاء فيه لفظي فقط",
     "en": "That is, the pronoun with its verb, since it is connected in both wording and meaning, unlike the like of “ḥarakatun” and “tarikatun”, where the connection of the tāʾ is merely verbal;"},
    {"type": "pair",
     "ar": "على أن اجتماع الحركات فيما ذكر ليس في البناء؛ لأن وضع الكلمات على الوقف بخلاف \"ضربن\".",
     "en": "besides, the concurrence of vowels in what was mentioned is not in the base form, since words are coined in the pausal state, unlike “ḍarabna”."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "عن مثل خروجه عن الحكم المذكور، فإنه أيضا مبني على الفتح،",
     "en": "Against the like of its departing from the stated rule, for it too is indeclinable on the fatḥa;"},
    {"type": "pair",
     "ar": "ولا معنى للفتحة التقديرية فيه؛ لأنه إنما يصار إليه للتعذر لفظا، ولا تعذر ههنا؛",
     "en": "and an implied fatḥa makes no sense in it, for one resorts to that only when [the overt vowel] is impossible, and there is no impossibility here;"},
    {"type": "pair",
     "ar": "لأن اتصال الضمير فيه بعد صيغة الماضي بخلاف \"غلامي\"، فإن الإضافة فيه مقدمة على تركيبه بالفعل، فافهم ولا تخبط.",
     "en": "for the pronoun is attached in it after the past-tense form, unlike “ghulāmī”, where the annexation precedes its composition with the verb. So understand, and do not blunder."},
]
