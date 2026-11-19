# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 179 (printed ١٧٨)."""

PAGE_NUMBER = 179
PRINTED_PAGE = "١٧٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(إلا إذا كان الخبر ظرفا[[١]]) أي: ليس أمره كأمر خبر المبتدأ في تقديمه إلا إذا كان ظرفا،",
     "en": "(Except when the predicate is an adverbial [ẓarf]); that is, its status is not like the status of the predicate of the subject with respect to its being placed first, except when it is an adverbial,"},
    {"type": "matn",
     "ar": "فإن حكمه إذا حكمه في جواز التقديم إذا كان الاسم معرفة، نحو قوله تعالى: ﴿إن إلينا إيابهم﴾[[٢]]،",
     "en": "for its rule is then its [the subject’s predicate’s] rule in the permissibility of placing it first when the noun [of inna] is definite, as in the words of Him, the Exalted: “Indeed, to Us is their return” (inna ilaynā iyābahum),"},
    {"type": "matn",
     "ar": "وفي وجوبه إذا كان الاسم نكرة[[٣]] نحو: «إن من البيان لسحرا، وإن من الشعر لحكمة»،",
     "en": "and in its being obligatory when the noun is indefinite, as in: “Indeed, in eloquence there is magic, and indeed, in poetry there is wisdom” (inna min al-bayāni la-siḥran, wa-inna min al-shiʿri la-ḥikmatan)."},
    {"type": "matn",
     "ar": "وذلك لتوسعهم[[٤]] في الظروف ما لا يتوسع في غيرها.",
     "en": "That is because of their allowing latitude (tawassuʿ) with adverbials to a degree not allowed with anything else."},

    {"type": "section", "ar": "[ خبر لا لنفي الجنس ]",
     "en": "The Predicate of the “Lā” That Negates the Genus"},

    {"type": "matn",
     "ar": "(خبر «لا» التي) الكائنة (لنفي الجنس[[٥]]) أي: لنفي صفته؛ إذ «لا رجل قائم» مثلا لنفي القيام عن الرجل لا لنفي الرجل نفسه",
     "en": "(The predicate of the “lā” that) is (for negating the genus [li-nafy al-jins]); that is, for negating its attribute—since “No man is standing” (lā rajula qāʾimun), for example, is for negating standing of the man, not for negating the man himself—"},
    {"type": "matn",
     "ar": "(هو المسند) إلى شيء آخر، هذا شامل لخبر المبتدأ أو خبر «إن» أو «كأن» وغيرها",
     "en": "(is that which is predicated) of something else—this covers the predicate of the subject, or the predicate of “inna” or “kaʾanna,” and others—"},
    {"type": "matn",
     "ar": "(بعد دخولها) أي: بعد دخول «لا»، فخرج به سائر الأخبار.",
     "en": "(after its entry), that is, after the entry of “lā”; by this all other predicates are excluded."},
    {"type": "matn",
     "ar": "والمراد بدخولها ما عرفت في خبر «إن»، فلا يرد نحو: «يضرب» في «لا رجل يضرب أبوه».",
     "en": "What is meant by its entry is what you learned regarding the predicate of “inna”; so such as “yaḍribu” in “No man—his father strikes” (lā rajula yaḍribu abūhu) does not constitute an objection."},
    {"type": "matn",
     "ar": "(نحو: «لا غلام رجل ظريف»). إنما عدل[[٦]] عن المثال المشهور، وهو",
     "en": "(As in: “No man’s servant is clever,” lā ghulāma rajulin ẓarīfun). He departed from the well-known example only—and it is…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "استثناء مفرغ. والتقدير: إلا في تقديمه في كل حال من أحوال الخبر إلا إذا كان ظرفا.",
     "en": "[It is] an emptied exception (istithnāʾ mufarragh). The implied sense is: “except in its being placed first in every one of the states of the predicate, except when it is an adverbial.”"},
    {"type": "pair",
     "ar": "ويجوز أن يكون استثناء من معنى الكلام.",
     "en": "It may also be an exception from the sense of the statement."},
    {"type": "pair",
     "ar": "والحاصل: أن أخبار هذه الحروف تخالف خبر المبتدأ في جواز التقديم في الأوقات كلها إلا وقت كونه ظرفا.",
     "en": "The upshot is that the predicates of these particles differ from the predicate of the subject in the permissibility of being placed first at all times, except at the time of its being an adverbial."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة الغاشية:٢٥.",
     "en": "Qurʾān, Sūrat al-Ghāshiya 88:25."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فيه بحث؛ لأن «إن» يصحح وقوع النكرة مبتدأ، صرح به الشيخ عبد القاهر في دلائل الإعجاز،",
     "en": "This is open to discussion, because “inna” makes valid the occurrence of an indefinite noun as subject; Shaykh ʿAbd al-Qāhir stated this explicitly in Dalāʾil al-iʿjāz."},
    {"type": "pair",
     "ar": "فليس حكمه إلا جواز التقديم، فقول المصنف: «إلا إذا كان ظرفا» قاصر.",
     "en": "So its rule is nothing but the permissibility of placing first; hence the author’s statement “except when it is an adverbial” falls short."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وذلك لأن كل محدث لا بد أن يكون في زمان أو مكان،",
     "en": "That is because every originated thing must be in a time or a place;"},
    {"type": "pair",
     "ar": "فصار الظرف مع الشيء كالقريب المحرم للشخص يدخل حيث لا يدخل غيره من الأجنبي،",
     "en": "so the adverbial has become, with respect to a thing, like a close relative within the prohibited degrees (al-qarīb al-maḥram) to a person, who enters where no one else, a stranger, may enter."},
    {"type": "pair",
     "ar": "وأجري الجار والمجرور مجراه لمناسبته للظرف؛ إذ كل ظرف في التقدير جار ومجرور.",
     "en": "The preposition and its object (al-jārr wa-l-majrūr) were treated in the same way, because of its affinity with the adverbial; for every adverbial is, in its underlying form, a preposition and its object."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إذا دخلت على النكرة.",
     "en": "When it enters upon an indefinite noun."},
    {"type": "pair",
     "ar": "وإنما عملت عمل «إن»؛ لأنها تشابه «إن» في إفادة المبالغة، فإن «لا» لمبالغة النفي، و«إن» لمبالغة الإثبات، فيكون من باب حمل النظير على النظير.",
     "en": "It governs as “inna” governs only because it resembles “inna” in conveying emphasis: “lā” is for emphatic negation and “inna” for emphatic affirmation; so it belongs to the category of assimilating a counterpart to its counterpart (ḥaml al-naẓīr ʿalā al-naẓīr)."},
    {"type": "pair",
     "ar": "وقيل: لأن «لا» نقيض «إن»، فيكون من باب حمل النقيض على النقيض.",
     "en": "It has also been said: because “lā” is the contradictory of “inna,” so it belongs to the category of assimilating a contradictory to its contradictory (ḥaml al-naqīḍ ʿalā al-naqīḍ)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "قال المصنف: ليس تمثيل النحاة بـ«لا رجل ظريف» حسنا؛ لأن «ظريف» في الظاهر صفة اسم «لا»؛ لأن خبر «لا» يحذف كثيرا.",
     "en": "The author said: the grammarians’ use of “lā rajula ẓarīfun” as an example is not good, because “ẓarīf” is, on its face, an adjective of the noun of “lā,” since the predicate of “lā” is frequently elided."},
    {"type": "pair",
     "ar": "والمثال ينبغي أن يكون ظاهرا فيما يمثل له.",
     "en": "An example ought to be clear with respect to what it exemplifies."},
    {"type": "pair",
     "ar": "وفي مثالنا لا يحتمل ظريف إلا الخبر؛ لأن المضاف المنفي بـ«لا» لا يوصف إلا بمنصوب.",
     "en": "In our example, “ẓarīf” can only be the predicate, because a construct noun negated by “lā” is qualified only by an accusative."},
    {"type": "pair",
     "ar": "واعترض عليه بأن ذلك مذهب جماعة منهم. وأما الآخرون فقد جوزوا الرفع حملا على المحل كما في توابع اسم «إن».",
     "en": "It was objected against him that this is the doctrine of [only] a group of them; as for the others, they permitted the nominative, by construing it with the [syntactic] position (ḥamlan ʿalā al-maḥall), as with the dependents (tawābiʿ) of the noun of “inna.”"},
]
