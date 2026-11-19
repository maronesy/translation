# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 443 (printed ٤٤٢)."""

PAGE_NUMBER = 443
PRINTED_PAGE = "٤٤٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «أي: غير زائدة ولا منقلبة عن» at the foot of PDF p. 442 (mid-sentence).
    {"type": "matn",
     "ar": "أصلية أو زائدة (تثبت) الهمزة في الأشهر لأصالتها كـ«قراء» بضم القاف وتشديد الراء لجيد القراءة، أو للمتنسك من قراء إذا تنسك[[١]].",
     "en": "…a radical or an augmentative [letter], (it remains), the hamza, in the best-known usage, because of its being radical, as in “qurrāʾ”, with a ḍamma on the qāf and a doubled rāʾ, for one who recites well, or for the devout, from “qaraʾa” when one becomes devout."},
    {"type": "matn",
     "ar": "وحكى أبو علي عن بعض العرب قلبها واوا نحو: «قراوان»",
     "en": "Abū ʿAlī reported from some of the Arabs its conversion into a wāw, as in “qurrāwān”."},
    {"type": "matn",
     "ar": "(وإن كانت) الهمزة (للتأنيث) أي: منقلبة عن ألف التأنيث كـ«حمراء»، فإن أصلها كان «حمرا» بألفين، إحداهما: للمد في الصوت، والثانية: للتأنيث،",
     "en": "(And if it is), the hamza, (for the feminine), that is, converted from the alif of the feminine, as in “ḥamrāʾ” (red, fem.), for its origin was “ḥamrā” with two alifs, one of them for prolonging the sound and the second for the feminine;"},
    {"type": "matn",
     "ar": "فقلبت الثانية همزة لوقوعها طرفا بعد ألف زائدة (قلبت واوا) فيقال: «حمراوان»؛",
     "en": "the second was converted into a hamza because it falls at the end after an augmentative alif, (it is converted into a wāw), so one says “ḥamrāwān”,"},
    {"type": "matn",
     "ar": "لأن الهمزة حرف ثقيل من جنس الألف، فينبغي ألا تقع بين الألفين مع أنها غير أصلية،",
     "en": "because the hamza is a heavy letter of the same kind as the alif, so it ought not to fall between two alifs, given that it is not radical;"},
    {"type": "matn",
     "ar": "والواو أقرب إلى الهمزة من الياء لثقلها، ولهذا قلبت الواو همزة في مثل: «أقتت وأجوه»، وربما صححت فقيل: «حمراءان».",
     "en": "and the wāw is closer to the hamza than the yāʾ is, because of its heaviness; for this reason the wāw is converted into a hamza in the like of “uqqitat” and “ujūh”. Sometimes it is left sound, and one says “ḥamrāʾān”."},
    # REVIEW: printed «وحكي المبرد» (final dotted yāʾ), whereas the parallel clause above has «وحكى أبو علي»; transcribed as printed, translated as «وحكى».
    {"type": "matn",
     "ar": "وحكي المبرد عن المازني قلبها ياء نحو: «حمرايان»، والأعرف قلبها واوا.",
     "en": "Al-Mubarrad reported from al-Māzinī its conversion into a yāʾ, as in “ḥamrāyān”; but the better-known [usage] is its conversion into a wāw."},
    {"type": "matn",
     "ar": "(وإلا) أي: وإن لم تكن الهمزة أصلية ولا للتأنيث بأن تكون للإلحاق كـ«علباء»[[٢]]؛ فإن همزته للإلحاق بـ«قرطاس»،",
     "en": "(Otherwise), that is, if the hamza is neither radical nor for the feminine, in that it is for attachment (ilḥāq), as in “ʿilbāʾ”, for its hamza is for attachment to [the pattern of] “qirṭās”;"},
    {"type": "matn",
     "ar": "أو منقلبة عن واو أو ياء أصلية كـ«كساء ورداء»، فإن أصلهما: «كساو ورداي»",
     "en": "or is converted from a radical wāw or yāʾ, as in “kisāʾ” (garment) and “ridāʾ” (cloak), whose origins are “kisāw” and “ridāy”,"},
    {"type": "matn",
     "ar": "(فالوجهان) المذكوران جائزان:",
     "en": "(then the two ways) mentioned are both permitted:"},
    {"type": "matn",
     "ar": "أحدهما: ثبوت الهمزة وبقاؤها؛ لأن الهمزة في الصورة الأولى منقلبة عن واو أو ياء ملحقة[[٣]] بالأصل، وفي الأخرى عن أصلية،",
     "en": "the first of them is the hamza’s remaining and staying, because the hamza in the first case is converted from a wāw or yāʾ that attaches [the word] to the radical [pattern], and in the other from a radical [letter];"},
    {"type": "matn",
     "ar": "فشابهتا همزة «قراء» فثبتت في الصورتين كما في «قراء».",
     "en": "so they resemble the hamza of “qurrāʾ”, and it remains in both cases as in “qurrāʾ”."},
    {"type": "matn",
     "ar": "وثانيهما: قلب الهمزة واوا؛ لأن عين الهمزة في الصورتين ليست بأصلية، فشابهت همزة «حمراء»، فانقلبت مثلها واوا،",
     "en": "The second of them is converting the hamza into a wāw, because the hamza itself in both cases is not radical; so it resembles the hamza of “ḥamrāʾ” and is converted into a wāw like it."},
    {"type": "matn",
     "ar": "في الترجمة الشريفية أن اللازم من هذه العبارة أنه لا يجوز أن يقال في «رداء» إلا «رداءان» بالهمزة، أو «رداوان» بالواو،",
     "en": "In al-Tarjama al-Sharīfiyya [it is said] that what follows from this wording is that one may say for “ridāʾ” only “ridāʾān” with the hamza or “ridāwān” with the wāw;"},
    {"type": "matn",
     "ar": "لكن المشهور «ردايان» بالياء، فكان ينبغي أن يقول المصنف: «وإلا فوجهان» بغير لام العهد؛",
     "en": "but the well-known form is “ridāyān” with the yāʾ, so the author ought to have said “otherwise, two ways”, without the lām of prior reference (ʿahd),"},
    {"type": "matn",
     "ar": "ليكون عبارة عن إثبات الهمزة، وردها إلى الأصل لا إشارة إلى الوجهين المذكورين -كما هو المتبادر من اللام-",
     "en": "so that it would express keeping the hamza and restoring it to the origin, not refer to the two ways mentioned, as is what first comes to mind from the lām;"},
    {"type": "matn",
     "ar": "لكنا قد تصفحنا كتب الثقاة كالمفصل والمفتاح واللباب، فما وجدنا فيها أثرا مما حكم باشتهاره غير ما وقع في شرح الرضي من أنه قد تقلب",
     "en": "but we have looked through the books of the reliable authorities, such as al-Mufaṣṣal, al-Miftāḥ and al-Lubāb, and found in them no trace of what he judged to be well known, other than what occurs in the commentary of al-Raḍī, that it is sometimes converted…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وهذا سهو.",
     "en": "This is an oversight."},
    {"type": "pair",
     "ar": "في القاموس: القراء ككتان الحسن القراءة جمع قراؤن، ولا يكسر وكرمان الناسك المتعبد كالقارئ والمقرئ جمعه قراؤن وقرارئ كمصابيح.",
     "en": "In al-Qāmūs: “al-qarrāʾ”, like “kattān”, is one who recites well, plural “qarrāʾūn”, and it has no broken plural; and [“al-qurrāʾ”], like “rummān”, is the devout worshipper, like “al-qāriʾ” and “al-muqriʾ”, its plural being “qurrāʾūn” and “qarāriʾ”, like “maṣābīḥ”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "العلباء: عصب العنق، وهما علباوان بينهما منبت العرف صحاح كذا نقله عنه.",
     "en": "Al-ʿilbāʾ: the sinew of the neck; they are two ʿilbāwān with the place where the mane grows between them. Al-Ṣiḥāḥ; so he cited it from it."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "صيغة اسم الفاعل نقل عنه هكذا في عبارة الرضي.",
     "en": "[It is] the active participle form; it is cited from him thus in the wording of al-Raḍī."},
    {"type": "pair",
     "ar": "ويفهم منه أن الحرف الزائد للإلحاق أولا في مثل علباء، هو الواو والياء، ثم عوض عنه الهمزة.",
     "en": "It is understood from this that the augmentative letter for attachment, originally, in the like of “ʿilbāʾ”, is the wāw or the yāʾ, and then the hamza was substituted for it."},
]
