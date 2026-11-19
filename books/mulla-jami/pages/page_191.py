# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 191 (printed ١٩٠)."""

PAGE_NUMBER = 191
PRINTED_PAGE = "١٩٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # The closing guillemet after «فداء» has no opening one on the page; kept as printed.
    {"type": "matn",
     "ar": "فداء﴾[[١]] أي: إما تمنون منا بعد الشد وإما تفدون فداء».",
     "en": "…ransom,” that is: either you grant favour after the securing, or you take ransom."},
    {"type": "matn",
     "ar": "(ومنها) أي: من تلك المواضع (ما وقع) أي: موضع مفعول مطلق وقع (للتشبيه) أي: لأن يشبه به أمر[[٢]] آخر.",
     "en": "(And among them)—that is, among those places—is (what occurs), that is, the place of an absolute object that occurs (for comparison—li-l-tashbīh), that is: so that another matter may be likened to it."},
    {"type": "matn",
     "ar": "واحترز به عن نحو: «لزيد صوت صوت حسن»[[٣]]؛ لأنه لم يقع للتشبيه",
     "en": "By this he guarded against such as “Zayd has a voice, the voice of a handsome one” (li-Zaydin ṣawtun ṣawta ḥasanin), because it does not occur for comparison;"},
    {"type": "matn",
     "ar": "(علاجا[[٤]]) أي: حال كونه دالا على فعل من أفعال الجوارح.",
     "en": "(as a bodily act—ʿilājan), that is: in the state of its indicating an act among the acts of the limbs."},
    {"type": "matn",
     "ar": "واحترز به عن نحو: «لزيد زهد زهد الصلحاء»؛ لأن الزهد ليس من أفعال الجوارح",
     "en": "By this he guarded against such as “Zayd has asceticism, the asceticism of the righteous” (li-Zaydin zuhdun zuhda al-ṣulaḥāʾ), because asceticism (zuhd) is not among the acts of the limbs;"},
    {"type": "matn",
     "ar": "(بعد جملة). احترز به عن نحو: «صوت زيد صوت حمار»[[٥]]",
     "en": "(after a sentence—baʿda jumlatin). By this he guarded against such as “Zayd’s voice is the voice of a donkey” (ṣawtu Zaydin ṣawtu ḥimārin);"},
    {"type": "matn",
     "ar": "(مشتملة) تلك الجملة (على اسم[[٦]]) كائن (بمعناه) أي: بمعنى المفعول المطلق.",
     "en": "(containing)—that sentence—(a noun—ʿalā ismin) that is (in its sense—bi-maʿnāhu), that is: in the sense of the absolute object."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة محمد: ٤.",
     "en": "Qurʾān, Sūrat Muḥammad 47:4."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: لأن يشبه بما ناب منابه أمر، فإنه الواقع بعد الجملة بحسب الظاهر لا المفعول المطلق.",
     "en": "That is: so that a matter may be likened to what stands in its stead; for that is what occurs after the sentence in outward form, not the absolute object."},
    {"type": "pair",
     "ar": "لا يقال: فإذن يخرج عن الضابطة إذا ذكر المفعول المطلق نفسه؛",
     "en": "It should not be said: then it falls outside the criterion when the absolute object itself is mentioned;"},
    {"type": "pair",
     "ar": "لأنا نقول: قد جرت عادتهم على حذفه، ولزوم مصدر في موضعه.",
     "en": "for we say: their custom has been to elide it, and to keep a maṣdar necessarily in its place."},
    {"type": "pair",
     "ar": "فعلى هذا لو فسر قوله: ما وقع للتشبيه بموضع مصدر وقع؛ لأن يشبه به أمر لسلم عن المناقشة.",
     "en": "On this basis, had he explained his words “what occurs for comparison” as “the place of a maṣdar that occurs so that a matter may be likened to it,” it would have been safe from dispute."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قال سيبويه: يجب في مثله الرفع على أنه بدل أو وصف لكونه مع وصفه كاسم واحد كما جعلوا الحال الموطئة حالا؛",
     "en": "Sībawayh said: in its like the nominative is required, as a substitute (badal) or as a qualifier, because together with its qualifier it is like a single noun, just as they made the preparatory circumstantial (al-ḥāl al-muwaṭṭiʾa) a ḥāl;"},
    {"type": "pair",
     "ar": "لأن في وصفه معنى الحالية، ولذلك لم يجعله تأكيدا لفظيا؛ لأنه يفيد ما لم يفده الأول.",
     "en": "because in its qualifier there is the sense of the ḥāl; and for that reason he did not make it a verbal corroboration (taʾkīd lafẓī), since it conveys what the first did not."},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: لا منع عندي من أن يكون تأكيدا، وإذا ترك المصدر وأتى بالوصف نحو: «له صوت حسن»، فالأولى الاتباع، ويجوز النصب على حذف الموصوف.",
     "en": "Shaykh al-Raḍī said: I see nothing preventing it from being a corroboration; and when one leaves out the maṣdar and brings the qualifier, as in “He has a fine voice,” concord (itbāʿ) is preferable, and the accusative is allowed on the elision of the qualified noun."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ليس في كثير من النسخ. ولم يكن في نسخة الشيخ الرضي.",
     "en": "[This word] is not in many of the copies, and it was not in Shaykh al-Raḍī’s copy."},
    {"type": "pair",
     "ar": "ولذا قال: ولا بد من شرط آخر، وهو أن يكون الاسم عارضا غير لازم ليدل على معنى الفعل المقدر أعني: الحدث، فيخرج نحو: «لزيد زهد زهد الصلحاء».",
     "en": "For this reason he said: another condition is necessary, namely that the noun be accidental, not inseparable, so that it indicate the sense of the supposed verb—I mean, the event (ḥadath); so such as “Zayd has asceticism, the asceticism of the righteous” is excluded."},
    {"type": "pair",
     "ar": "ولا يخفى أنه لا يخرج نحو: «له حركة في المعقولات حركة في المحسوسات»، بخلاف اشتراط كونه علاجا، فإنه أيضا يخرج.",
     "en": "It is not hidden that such as “He has a movement among intelligibles, a movement among sensibles” is not excluded [by that condition]; unlike the stipulation of its being a bodily act, for by that it too is excluded."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "جوز نصبه على الحالية، ورفعه على أنه بدل، أو عطف بيان، أو صفة بتقدير مثل، أو بتأويله بمنكر هذا إذا كان منكرا.",
     "en": "He allowed its accusative as a ḥāl, and its nominative as a substitute, or an explicative apposition (ʿaṭf bayān), or a qualifier on the supposition of “mithl” (like), or by interpreting it as indefinite—this when it is indefinite."},
    {"type": "pair",
     "ar": "أما إذا عرف فرفعه لا يكون بالوصفية إلا عند الخليل؛ لأنه بتقدير مثل، وهو لا يعرف بالإضافة.",
     "en": "But when it is definite, its nominative is not as a qualifier except according to al-Khalīl; because it is on the supposition of “mithl,” and that does not become definite by annexation."},
    {"type": "pair",
     "ar": "وإنما لم يجوز الجمهور أن يكون العامل المصدر المذكور؛ لأنه لا يصلح تأويله بـ«أن» مع الفعل وعمله لهذا التأويل،",
     "en": "The majority did not allow the governor to be the mentioned maṣdar only because it is not fit to be interpreted as “an” with the verb, while its governing is by virtue of this interpretation;"},
    {"type": "pair",
     "ar": "وإنما لم يجز؛ لأن «أن» مع الفعل مرجو، وهو في هذا المقام مقطوع به.",
     "en": "and it is not allowed only because “an” with the verb [denotes what is] hoped for, whereas in this context it is certain."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "إنما اشترط ذلك ليدل على الفعل المقدر، فإن الجملة باشتمالها على الاسم تدل على نفس الفعل، وباشتمالها على صاحبها تدل على ما لا بد للفعل منه أعني: الفاعل.",
     "en": "He stipulated this only so that it would indicate the supposed verb; for the sentence, by containing the noun, indicates the verb itself, and by containing its possessor, indicates what the verb cannot do without—I mean, the agent."},
    {"type": "pair",
     "ar": "قال سيبويه: هذه الدلالة تغني غناء التقدير، وحسنه الشيخ الرضي.",
     "en": "Sībawayh said: this indication suffices in place of supposition; and Shaykh al-Raḍī approved it."},
    {"type": "pair",
     "ar": "إن قيل: لم لم يجعلوا الاسم المذكور عاملا كما قال بعضهم.",
     "en": "If it is asked: why did they not make the mentioned noun the governor, as some said?"},
    {"type": "pair",
     "ar": "أجيب: بأن المصدر عندهم لا يعمل إلا إذا صح تقديره بـ«أن» وفعل منه، ويسمج ذلك في «مررت به»، فإذا له صوت؛",
     "en": "It was answered that the maṣdar, according to them, does not govern unless it may validly be construed as “an” with a verb from it; and that is ungainly in “I passed by him, and behold, he had a voice,”"},
    {"type": "pair",
     "ar": "لأنه قطع بوقوع الصوت، وأن يصوت ليس قطعا بوقوعه.",
     "en": "because the occurrence of the voice is certain there, whereas “that he voice” is not a certainty of its occurrence."},
]
