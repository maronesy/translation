# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 574 (printed ٥٧٣)."""

PAGE_NUMBER = 574
PRINTED_PAGE = "٥٧٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # PDF p. 573 ends with a complete sentence; this page opens a new one.
    {"type": "matn",
     "ar": "وقد يجاب بنفي كليهما؛ لاحتمال الخطأ في اعتقاد المتكلم بوجود أحدهما.",
     "en": "It is sometimes answered by negating both of them, because of the possibility of error in the speaker’s belief that one of them is the case."},
    {"type": "matn",
     "ar": "فالمشار إليه[[١]] بـ«ثم» في الموضعين أمر واحد، لكنه لما كان مشتملا على شرطين[[٢]] لصحة وقوع أم المتصلة، فرع عليه باعتبار كل واحد منهما حكما آخر،",
     "en": "So what is referred to by “thumma” [in “min thamma”, hence] in the two places is one thing; but since it comprises two conditions for the validity of the connected “am”, he derived from it, in respect of each of them, a further ruling;"},
    {"type": "matn",
     "ar": "وجعلها إشارة في كل موضع إلى شرط آخر لا يخلو عن سماجة[[٣]]،",
     "en": "and making it a reference in each place to a different condition is not free of awkwardness."},
    {"type": "matn",
     "ar": "ولو اقتصر على قوله: «ومن ثم لم يجز» في أول الكلام، وعطف قوله: «كان جوابها بالتعيين» على قوله: «لم يجز»، وتعلق كل حكم بشرط على طريق اللف والنشر، لكان أخصر وأحسن[[٤]]، كما لا يخفى.",
     "en": "Had he confined himself to his words “hence it is not permissible” at the beginning of the statement, and coordinated his words “its answer is by specification” with his words “it is not permissible”, each ruling attaching to a condition by way of involution and evolution (al-laff wa-l-nashr), it would have been more concise and better, as is evident."},
    {"type": "matn",
     "ar": "(و«أم» المنقطعة كـ«بل») في الإضراب عن الأول[[٥]] (و) مثل (الهمزة) للشك في الثاني[[٦]]،",
     "en": "(And the disconnected “am” (al-munqaṭiʿa) is like “bal”) in turning away (iḍrāb) from the first, (and) like (the hamza) for doubt about the second;"},
    {"type": "matn",
     "ar": "والواقع قبلها إما خبر (مثل) قولك: (إنها لإبل أم شاء؟) أي: إن القطيعة[[٧]] التي أراها لإبل، وهي جملة خبرية،",
     "en": "what occurs before it is either a statement, (as in) your saying (“innahā la-ibilun am shāʾun?”, they are camels, or are they sheep?), that is: the herd that I see is camels, which is a declarative sentence;"},
    {"type": "matn",
     "ar": "فلما علمت أنها ليست بـ«إبل» أعرضت عن هذه الإخبار، ثم شككت في أنها شاء، أو شيء آخر، فاستفهمت عنها بقولك: «أم شاء؟» أي: بل أهي شاء؟",
     "en": "then, when you learned that they were not camels, you turned away from this statement, and then doubted whether they were sheep or something else, and asked about them by saying “am shāʾun?”, that is, “rather, are they sheep?”"},
    {"type": "matn",
     "ar": "وإما استفهام كما تقول: «أزيد عندك أم عمرو؟» أي: بل أعمرو، حين يقصد الإضراب عن الاستفهام الأول بالاستفهام الثاني.",
     "en": "Or [what precedes it] is a question, as when you say “is Zayd with you, or ʿAmr?”, that is, “rather, is it ʿAmr?”, when turning away from the first question to the second question is intended."},
    {"type": "matn",
     "ar": "(و«إما» قبل المعطوف عليه لازمة مع «إما») أي: غير مستعملة[[٨]] إلا معها، يعني:",
     "en": "(And “immā” before the term coordinated upon is bound up with “immā”), that is, it is not used except with it; that is to say,…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "تفريع على تفسير ثم في الموضعين بمعنى واحد.",
     "en": "This is a consequence of interpreting “thamma” in the two places in one sense."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أحدهما: أن يكون ما يليها أحد المستويين، والآخر الهمزة، والمفرع عليه عدم جواز التركيب المذكور.",
     "en": "The first: that what follows it be one of the two equivalents, and the other follow the hamza; what is derived from it is the impermissibility of the construction mentioned."},
    {"type": "pair",
     "ar": "والثاني: لطلب التعيين، والمفرع عليه كان جوابا بالتعيين.",
     "en": "The second: [that it be] for requesting specification; what is derived from it is [its answer] being by specification."},
    # REVIEW: printed «كان جوابا بالتعيين» (not «كون جوابها»); transcribed as printed.

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لأن المذكور سابقا حكم واحد لا حكمان حتى يشار لكل منهما استقلالا، وفيه رد على الفاضل الهندي،",
     "en": "For what was mentioned previously is one ruling, not two rulings such that each of them could be referred to independently; and in this is a rejoinder to al-Fāḍil al-Hindī."},
    {"type": "pair",
     "ar": "لكن فيه أن إعادة اسم الإشارة يقتضي أن يكون المشار إليه بالثاني غير الأول دفعا للتكرار.",
     "en": "But against this [it may be said] that repeating the demonstrative requires that what is referred to by the second be other than the first, so as to avoid repetition."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لكن ما ذكره المصنف أظهر لعدم الاحتمال فيه على جعل كل واحد منهما إشارة إلى شرط.",
     "en": "But what the author stated is clearer, since, on making each of them refer to a condition, there is no ambiguity in it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سواء كان لتدارك الغلط كما في مثال المتن أو لمجرد الانتقال من كلام إلى كلام، كما في قوله تعالى: ﴿أم يقولون افتراه﴾ (يونس:٣٨)،",
     "en": "Whether it is to correct an error, as in the example of the text, or merely to pass from one statement to another, as in His words, the Exalted: “Or do they say, ‘He has invented it’?” (Qurʾān, Sūrat Yūnus 10:38);"},
    {"type": "pair",
     "ar": "فلا يليها إلا الجملة: إما ظاهرة الجزأين نحو: أزيد عندك أم عمرو عندك؟ أو مقدرة أحدهما كما في مثال المتن.",
     "en": "so nothing follows it but a sentence, either with both its parts explicit, as in “is Zayd with you, or is ʿAmr with you?”, or with one of them implied, as in the example of the text."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "هذا بالنظر إلى أصل المعنى؛ لأن الهمزة المقدرة للاستفهام قد تجيء للإنكار نحو: ﴿أم يقولون افتراه﴾ (يونس:٣٨).",
     "en": "This is with regard to the basic meaning, for the implied interrogative hamza sometimes comes for disavowal (inkār), as in “Or do they say, ‘He has invented it’?” (Qurʾān, Sūrat Yūnus 10:38)."},
    {"type": "pair",
     "ar": "وقد تجيء بمعنى بل وحده كقوله تعالى: ﴿أم أنا خير من هذا﴾ (الزخرف:٥٢)، ونحو: ﴿أم هل تستوي الظلمات والنور﴾ (الرعد:١٦).",
     "en": "And it sometimes comes in the sense of “bal” alone, as in His words, the Exalted: “Or am I not better than this one?” (Qurʾān, Sūrat al-Zukhruf 43:52), and as in “Or are darkness and light equal?” (Qurʾān, Sūrat al-Raʿd 13:16)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "هي الطائفة من البقر والغنم، والجمع أقاطيع على غير قياس، كأنهم جمعوا قطيعا، كذا في الصحاح.",
     "en": "It is a group of cattle or sheep; the plural is aqāṭīʿ, irregularly, as though they had pluralized quṭīʿ; so in al-Ṣiḥāḥ."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "إما العاطفة إلا مع إما قبل المعطوف أفاد أن اللزوم بالمعنى المتعارف من حيث الاستعمال.",
     "en": "[That is, the coordinating] “immā” [is not used] except with an “immā” before the coordinated term; he indicated that “being bound” is in the customary sense, with respect to usage."},
]
