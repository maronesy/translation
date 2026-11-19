# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 258 (printed ٢٥٧)."""

PAGE_NUMBER = 258
PRINTED_PAGE = "٢٥٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وأما» from the foot of PDF p. 257.
    {"type": "matn",
     "ar": "إذا جعلته داخلا[[١]] في العامل المعنوي كما هو الظاهر من كلامهم، فالمراد هو الاحتمال الثاني لا غير[[٢]].",
     "en": "…if you take it as included in the governor of meaning, as is apparent from their words, then what is meant is the second interpretation and nothing else."},
    {"type": "matn",
     "ar": "(و) كما لا تتقدم الحال على العامل المعنوي كذلك (لا) يتقدم (على) ذي الحال (المجرور[[٣]]) سواء كان مجرورا بالإضافة[[٤]] أو بحرف الجر،",
     "en": "(And) just as the ḥāl does not precede a governor of meaning, so it does (not) precede (a genitive) dhū al-ḥāl (the owner of the ḥāl), whether it is in the genitive by annexation (iḍāfa) or by a preposition."},
    {"type": "matn",
     "ar": "فإن كان مجرورا بالإضافة لم يتقدم الحال عليه اتفاقا[[٥]]، نحو: «جاءتني مجردا عن الثياب ضاربة زيد»،",
     "en": "If it is in the genitive by annexation, the ḥāl does not precede it, by agreement, as in “Zayd’s striker came to me, [he being] stripped of clothes”;"},
    {"type": "matn",
     "ar": "وذلك لأن الحال تابع وفرع لذي الحال[[٦]]، والمضاف إليه لا يتقدم على المضاف، فلا يتقدم تابعه أيضا،",
     "en": "that is because the ḥāl is a dependent and branch of the dhū al-ḥāl, and the annexed noun (muḍāf ilayhi) does not precede the governing noun of annexation (muḍāf), so neither does its dependent."},
    {"type": "matn",
     "ar": "وإن كان مجرورا بحرف الجر ففيه خلاف، فسيبويه وأكثر البصرية يمنعون تقديمها عليه، للعلة المذكورة، وهو المختار عند المصنف، ولهذا قال: (على الأصح).",
     "en": "If it is in the genitive by a preposition, there is disagreement: Sībawayh and most of the Basrans forbid placing it before it, for the reason mentioned, and this is the view the author prefers; hence he said: (on the soundest [view])."},
    {"type": "matn",
     "ar": "ونقل عن بعضهم: الجواز استدلالا بقوله تعالى: ﴿وما أرسلناك إلا كافة للناس﴾[[٧]]،",
     "en": "Permissibility is reported from some of them, citing as evidence His words, the Exalted: “We have not sent you except as a deterrent to [all] people (kāffatan li-l-nās)”;"},
    {"type": "matn",
     "ar": "ولعل الفرق بين حرف الجر والإضافة: أن حرف الجر معد للفعل كالهمزة والتضعيف، فكأنه من تمام الفعل وبعض حروفه،",
     "en": "and perhaps the difference between the preposition and annexation is that the preposition makes the verb transitive, like the hamza and the doubling [of the middle radical], so it is as though part of the verb’s completion and one of its letters;"},
    {"type": "matn",
     "ar": "فإذا قلت: «ذهبت راكبة بهند» فكأنك قلت: «أذهبت راكبة هندا»، فالمجرور بحسب الحقيقة ليس مجرورا.",
     "en": "so when you say “dhahabtu rākibatan bi-Hindin” (I went with Hind, she riding), it is as though you said “adhhabtu rākibatan Hindan” (I took Hind away, she riding); thus the genitive is in reality not a genitive."},
    {"type": "matn",
     "ar": "وأجاب بعضهم عن هذا الاستدلال: بجعل «كافة» حالا عن الكاف[[٨]]، والتاء",
     "en": "Some answered this argument by taking “kāffatan” as a ḥāl of the kāf [the pronoun “you”], the tāʾ…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وإليه ذهب المصنف في شرحه.",
     "en": "This is the view the author took in his commentary."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لأن اللائق حينئذ استثناؤه عن العامل المعنوي لا أن يبين المخالفة بقوله: بخلاف الظرف.",
     "en": "For in that case the fitting thing would be to except it from the governor of meaning, not to state the contrast with his words “unlike the adverbial.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "المتبادر من عبارة المتن، ولا على العامل المجرور،",
     "en": "What first comes to mind from the wording of the matn is “nor [does it precede] a genitive governor.”"},
    {"type": "pair",
     "ar": "فالأنسب الأوضح أن يقال: ولا يتقدم على المجرور في الأصح، ولا على العامل المعنوي بخلاف الظرف.",
     "en": "So it would be more fitting and clearer to say: “nor does it precede the genitive, on the soundest [view], nor the governor of meaning, unlike the adverbial.”"},
    {"type": "pair",
     "ar": "وأما التقدم على ذي الحال المرفوع والمنصوب فجائز مطلقا عند البصريين، وممتنع عند الكوفيين إلا في مرفوع تقدم عامله على الحال.",
     "en": "As for preceding a nominative or accusative dhū al-ḥāl, it is permitted without restriction according to the Basrans, and forbidden according to the Kufans except with a nominative whose governor precedes the ḥāl."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "استثنى منه ما إذا كان المضاف جزء المضاف إليه، أو جاز قيام المضاف إليه مقامه، فإنه يجوز التقديم، لكن على قلة نحو: يتحرك ماشيا يد زيد، ونتبع حنيفا ملة إبراهيم.",
     "en": "Excepted from this is where the muḍāf is part of the muḍāf ilayhi, or where the muḍāf ilayhi may stand in its place; then placing it first is permitted, though rarely, as in “Zayd’s hand moves, [he] walking,” and “We follow, [he being] a ḥanīf, the creed of Abraham.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إلا إذا كان المضاف بحيث يمكن حذفه، وإقامة المضاف إليه مقامه نحو: ﴿واتبع ملة إبراهيم حنيفا﴾ (سورة النساء:١٢٥).",
     "en": "Except where the muḍāf is such that it can be elided and the muḍāf ilayhi put in its place, as in “and followed the creed of Abraham, a ḥanīf” (Qurʾān, Sūrat al-Nisāʾ 4:125)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "نقض بجواز «راكبا جاء زيد» مع عدم جواز تقديم ذي الحال.",
     "en": "This is countered by the permissibility of “Riding, Zayd came,” although placing the dhū al-ḥāl first is not permitted."},
    {"type": "pair",
     "ar": "ولك أن تعتذر بجواز تقديم ذي الحال لأداء هذا المعنى بعينه إلا أنه لا يسمى فاعلا، بل مبتدأ.",
     "en": "You may answer that placing the dhū al-ḥāl first to convey this very meaning is permitted, except that it is then called not a fāʿil but a mubtadaʾ."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "سورة سبأ: ٢٨.",
     "en": "Qurʾān, Sūrat Sabaʾ 34:28."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "والمعنى: ما أرسلناك إلا مانعا للناس عما يضرهم.",
     "en": "The meaning is: We have sent you only to restrain people from what harms them."},
    {"type": "pair",
     "ar": "إن قلت: إنه عليه السلام كما أرسل مانعا ناهيا أرسل آمرا فكيف يصح الحصر؟",
     "en": "If you say: just as he, peace be upon him, was sent as a restrainer and forbidder, he was sent as a commander; so how is the restriction (ḥaṣr) valid?"},
    {"type": "pair",
     "ar": "قلنا: الحصر إضافي لا حقيقي كما إذا جعلته حالا من الناس؛ لأنه صلى الله عليه وسلم مبعوث إلى الثقلين.",
     "en": "We say: the restriction is relative, not real, just as when you take it as a ḥāl of “people”; for he, may Allah bless him and grant him peace, was sent to both humankind and the jinn (al-thaqalayn)."},
    {"type": "pair",
     "ar": "إن قلت: الحال قيد للعامل، فيلزم أن يكون الكف في وقت",
     "en": "If you say: the ḥāl is a restriction on the governor, so it would follow that the restraining is at the time…"},
]
