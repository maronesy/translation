# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 120 (printed ١١٩)."""

PAGE_NUMBER = 120
PRINTED_PAGE = "١١٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "«أتين»[[١]] (كزيادته) أي: مثل زيادة حرف، أو حرف زائد في أول الفعل (غير قابل) أي: حال كون وزن الفعل[[٢]]، أو ما كان على وزن الفعل غير قابل (للتاء[[٣]])؛ لأنه يخرج الوزن بهذا التاء، لاختصاصها بالاسم[[٤]] عن أوزان الفعل.",
     "en": "[the letters of] “ataytu[na]” [i.e., the imperfect-prefix letters hamza, tāʾ, yāʾ, nūn]. (Like its augmentation): that is, like the augmentation of a letter, or an augmented letter, at the beginning of the verb, (not admitting) — that is, the verbal pattern being, or that which is upon the verbal pattern being, not admitting — (the tāʾ); because the pattern departs [from the verb-patterns] through this tāʾ, since it (the tāʾ) is peculiar to the noun, [and so it removes it] from the verbal patterns."},
    {"type": "matn",
     "ar": "ولو قال: غير قابل للتاء قياسا، بالاعتبار الذي امتنع من أجله من الصرف لم يرد عليه «أربع» إذا سمي به[[٥]] رجل، فإن لحوق التاء به للتذكير، فلا يكون قياسا، ولا «أسود»، فإن مجيء التاء في أسود للحية الأنثى ليس باعتبار الوصف الأصلي الذي لأجله يمتنع من الصرف، بل باعتبار غلبة الاسمية العارضة.",
     "en": "Had he said: “not admitting the tāʾ by rule (qiyāsan), in the very respect on account of which it is denied full inflection,” then neither “Arbaʿ” — when a man is named by it — would have been an objection against him, for the attachment of the tāʾ to it is [only] for [marking] the masculine and so is not by rule; nor would “Aswad,” for the coming of the tāʾ in “aswad” — [as in “aswada,” the name of] the female serpent — is not by consideration of the original descriptive sense on account of which it is denied full inflection, but by consideration of the accidental predominance of nounhood."},
    {"type": "matn",
     "ar": "(ومن ثمة) أي: ومن أجل اشتراط عدم قبول التاء[[٦]] (امتنع أحمر) عن الصرف؛ لوجود الزيادة المذكورة مع عدم قبول التاء.",
     "en": "(And from this) — that is, on account of the stipulation of not admitting the tāʾ — (“aḥmar” is denied) full inflection, because of the presence of the aforementioned augmentation together with its not admitting the tāʾ."},
    {"type": "matn",
     "ar": "(وانصرف يعمل) لقبوله التاء؛ لمجيء «يعملة» للناقة القوية على العمل والسير.",
     "en": "(And “yaʿmal” is fully inflected) because it admits the tāʾ, since “yaʿmala” occurs [as a name] for the she-camel strong in labor and travel."},
    {"type": "matn",
     "ar": "(وما فيه علمية مؤثرة) أي: كل اسم غير منصرف يكون فيه علمية مؤثرة في منع الصرف بالسببية المحضة، أو مع شرطية لسبب آخر[[٧]].",
     "en": "(And that in which there is operative proper-nounhood): that is, every imperfectly inflected noun in which there is a proper-nounhood operative in denying full inflection — whether by pure causality, or together with being a condition for another cause."},
    {"type": "matn",
     "ar": "واحترز بذلك[[٨]] عما يجامع ألفي التأنيث، أو صيغة منتهى الجموع، فإن كل واحد[[٩]] منهما كاف في منع الصرف، لا تأثير فيه للعلمية.",
     "en": "By that he guarded against what coincides with the two alifs of femininity (alifā al-taʾnīth), or the form of the ultimate plural (ṣīghat muntahā al-jumūʿ); for each of these two suffices by itself in denying full inflection, proper-nounhood having no effect therein."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إما في الحال أو في الأصل، كما في هرق أمرا مغيرا الأرق، ولو تصرف في الوزن بما يخرجه عن الوزن مع بقاء الزائد لم يضر.",
     "en": "[The augment is] either in the current state or in the original, as in “haraqa” — an element that alters “araqa” (to spill) [the hāʾ replacing the hamza]; and even if [the form] is modified in its pattern in a way that removes it from the [verbal] pattern while the augment remains, that does no harm."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "حال من ضمير «أوله». وإنما لم يجعله شرطا للشق الأول؛ لأنه لاختصاصه بالفعل لا يقبل التاء أصلا.",
     "en": "[It is] a circumstantial qualifier of the pronoun in “its beginning” (awwalihi). He did not make it a condition of the first branch only because, on account of its being peculiar to the verb, it does not admit the tāʾ at all."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "كأنه أراد غير قابل للتاء بحسب الوضع. فلا يرد النقض بـ«أسود»؛ إذ قياس مؤنثه أن يكون على فعلاء.",
     "en": "It is as though he intended “not admitting the tāʾ by original coinage (waḍʿ).” So the objection through “aswad” does not arise, since the rule for its feminine is that it be on the pattern faʿlāʾ [i.e., “sawdāʾ,” not with a tāʾ]."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: لأن الداخلة على الفعل هي الساكنة.",
     "en": "That is: because the [tāʾ] that attaches to the verb is the quiescent one (al-sākina)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أربع إذا سمي به لا يقبل التاء، فلا حاجة لدفعه إلى تقييد عدم القبول بقولنا: «قياسا»، إنما يحتاج إليه لتصحيح قول النحاة: إن انصراف «أربع» إنما هو لعدم أصالة الوصف.",
     "en": "“Arbaʿ,” when one is named by it, does not admit the tāʾ, so there is no need — in order to repel [the objection through it] — to restrict the non-admission by our saying “by rule.” It is needed only to vindicate the grammarians’ statement that the full inflection of “arbaʿ” is [precisely] on account of the descriptiveness not being original."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فيه أن وجود الشرط لا يستلزم انتفاء المشروط. فالأولى أن يقال: من أجل وجود وزن الفعل مع سبب آخر، وتحقق شرطه امتنع «أحمر» من الصرف.",
     "en": "Against this [it may be noted] that the existence of a condition does not entail the non-existence of the conditioned. So it is preferable to say: it is on account of the presence of the verbal pattern together with another cause, and the realization of its condition, that “aḥmar” is denied full inflection."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لا بالشرطية المحضة عند الجمهور خلافا لجماعة حيث قالوا: تأثير علمية الاسم الذي فيه الألف والنون ليس إلا لتحقق السبب فيه، وهو المشابهة بألف التأنيث الممدودة.",
     "en": "Not by pure conditionality, according to the majority — contrary to a group [of grammarians], who said: the effect of the proper-nounhood of a noun containing the [augmented] alif and nūn is nothing but [an index of] the realization in it of the [true] cause, namely resemblance to the extended alif of femininity (alif al-taʾnīth al-mamdūda)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: بقوله: مؤثرة عما، أي: عن علمية يجامع إلى آخره فهي صفة احترازية. قوله: بالسببية المحضة حال من فاعل مؤثرة.",
     "en": "That is, by his word “operative (muʾaththira)” [he guarded] against — that is, against a proper-nounhood that coincides [with the two alifs of femininity], and so forth; so it is a precautionary qualifier. His phrase “by pure causality” is a circumstantial qualifier of the agent of “operative.”"},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "علة مصححة للاحتراز عنهما، أي: فإن كلا من السببين كاف في منع الصرف بدون العلمية، فمثل حمراء وحضاجر إذا نكرا لم يصرفا.",
     "en": "[This is] a cause vindicating the guarding against these two, that is: each of the two causes suffices in denying full inflection without proper-nounhood; so the like of “ḥamrāʾ” and “ḥaḍājir,” when made indefinite, are not fully inflected."},
]
