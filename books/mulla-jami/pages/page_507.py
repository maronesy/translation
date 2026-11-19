# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 507 (printed ٥٠٦)."""

PAGE_NUMBER = 507
PRINTED_PAGE = "٥٠٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(و«اضرب») مثال» at the foot of PDF p. 506 (mid-sentence).
    {"type": "matn",
     "ar": "لما يكون بعده كسرة (و«اعلم») مثال لما يكون بعده فتحة.",
     "en": "…of that after which there is a kasra; (and “iʿlam”) is an example of that after which there is a fatḥa."},
    {"type": "matn",
     "ar": "(وإن كان رباعيا فمفتوحة) أي: فالهمزة مفتوحة؛ لأنها همزة أصل ردت لارتفاع موجب حذفها، وهو اجتماع همزتين في المتكلم الواحد، لا همزة وصل (مقطوعة) لذلك بعينه.",
     "en": "(And if it is quadriliteral, then [it is] with a fatḥa), that is, the hamza has a fatḥa, because it is an original hamza, restored on the removal of what necessitated its elision, namely the meeting of two hamzas in the first person singular; it is not a connective hamza (hamzat al-waṣl). ([It is] disjunctive) for that very same reason."},

    {"type": "section", "ar": "[فعل ما لم يسم فاعله]",
     "en": "The Verb Whose Agent Is Not Named (the Passive Verb)"},

    {"type": "matn",
     "ar": "(فعل ما لم يسم فاعله) أي: فعل المفعول[[١]] الذي لم يذكر فاعله، وإضافة الفاعل إليه لأدنى ملابسة، أو على حذف مضاف أي: فاعل فعله الواقع عليه،",
     "en": "(The verb of that whose agent is not named), that is, the verb of the object (mafʿūl) whose agent (fāʿil) is not mentioned. The annexation of “agent” to it is by virtue of the slightest connection, or is on the supposition of an elided first term of annexation, that is, “the agent of its verb that falls upon it”."},
    {"type": "matn",
     "ar": "ولا يبعد أن يراد بالموصول الفعل الذي لم يذكر فاعله، ويكون إضافة الفعل إليه بيانية.",
     "en": "It is not far-fetched that by the relative [“mā”] the verb whose agent is not mentioned is meant, the annexation of “verb” to it then being explicative (bayāniyya)."},
    {"type": "matn",
     "ar": "(هو ما حذف فاعله) وأقيم المفعول مقامه، ولم يذكر هذا القيد ههنا اكتفاء بذكره فيما سبق.",
     "en": "(It is that whose agent has been elided) and the object put in its place; he did not mention this qualification here, being content with having mentioned it earlier."},
    {"type": "matn",
     "ar": "(فإن كان) الفعل الذي أريد حذف فاعله وإقامة المفعول مقامه (ماضيا) غيرت صيغته[[٢]] دفعا للبس (ضم أوله وكسر ما قبل آخره) مثل: «ضرب، ودحرج، وأعلم واختير»،",
     "en": "(Then if) the verb whose agent is meant to be elided and its object put in its place (is a past [verb]), its form is changed to avert confusion: (its first [letter] is given a ḍamma and what precedes its last [letter] a kasra), as in “ḍuriba, wa-duḥrija, wa-uʿlima wa-ukhtīra”."},
    {"type": "matn",
     "ar": "هذا النوع من التغير؛ لأن معناه غريب[[٣]]، فاختير له وزن غريب لم يوجد في الأوزان؛ لخروج الضمة إلى الكسرة،",
     "en": "[It takes] this kind of change because its meaning is unusual, so an unusual pattern not found among the patterns was chosen for it, on account of the passing from the ḍamma to the kasra."},
    {"type": "matn",
     "ar": "ووزن فعل بالخروج من الكسرة إلى الضمة، وإن كان غريبا يدل على غرابة المعنى أيضا، لكن الخروج من الكسرة إلى الضمة أثقل[[٤]]، فلا ضرورة في اختياره بعد حصول المقصود بأخف منه.",
     "en": "The pattern fiʿul, with the passing from the kasra to the ḍamma, though it is unusual and would also indicate the unusualness of the meaning, involves a passage from the kasra to the ḍamma that is heavier; so there is no necessity to choose it once the purpose is achieved by what is lighter than it."},
    {"type": "matn",
     "ar": "(ويضم الثالث مع همزة الوصل[[٥]]) نحو: «أنطلق، وأقتدر، واستخرج» لئلا يلتبس[[٦]] في الدرج بالأمر من ذلك الباب",
     "en": "(And the third [letter] is given a ḍamma along with the connective hamza), as in “unṭuliqa, wa-uqtudira, wa-ustukhrija”, lest it be confused, in continuous speech, with the imperative of that verbal form;"},
    {"type": "matn",
     "ar": "(و) يضم (الثاني مع التاء) مثل: «تعلم، وتجوهل، وتدحرج» لئلا يلتبس بصيغة",
     "en": "(and) there is given a ḍamma to (the second along with the tāʾ), as in “tuʿullima, wa-tujūhila, wa-tuduḥrija”, lest it be confused with the form…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إنما أضيف الفعل إلى المفعول؛ لأنه مبني له كذا في الرضي.",
     "en": "The verb was annexed to the object only because it is constructed for it; so in al-Raḍī."},
    {"type": "pair",
     "ar": "فعلم أن إضافة الفعل إلى ما ليست لأدنى ملابسة، كما وهم.",
     "en": "So it is known that the annexation of “verb” to “mā” is not by virtue of the slightest connection, as has been wrongly supposed."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فيه إشارة إلى ما تقرر من أن المجهول فرع المعلوم؛ لأن الأصل الإسناد إلى الفاعل.",
     "en": "In it is an indication of what is established, that the passive is derived from the active, because the basic case is attribution to the agent."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إذ الفعل من ضرورة معناه ما يقوم به، فلما حذف منه ذلك خيف أن يلحق في أول وهلة النظر بقسم الأسماء، فجعل على وزن لا يكون في الأسماء.",
     "en": "For the verb, by the necessity of its meaning, has that in which it subsists; so when that was removed from it, it was feared that at first glance it would be classed with the nouns, and it was therefore put on a pattern that does not occur among the nouns."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "من خروج الضمة إلى الكسرة؛ لأن الأول خروج من أثقل إلى ثقيل بخلاف الثاني.",
     "en": "[Heavier] than passing from the ḍamma to the kasra, because the former is a passage from the heavier to the heavy, unlike the latter."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ظرف مستقر لا لغو؛ لأن ضمة الهمزة علم من قوله: ضم أوله وكذا مع التاء.",
     "en": "A stable adverbial (ẓarf mustaqarr), not a dependent one (laghw), because the ḍamma of the hamza is known from his words “its first is given a ḍamma”; and likewise “along with the tāʾ”."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "قدم العلة مع أنه تفسير لقوله: خوف اللبس ليكون كل حكم مقرونا مع علته،",
     "en": "He put the reason first, although it is an explanation of his words “for fear of confusion”, so that every ruling might be joined with its reason;"},
    {"type": "pair",
     "ar": "وأشار إلى كونه تفسيرا له بقوله: هذا علة لقوله: ويضم الثالث والثاني.",
     "en": "and he indicated its being an explanation of it by his words: “This is a reason for his words ‘and the third and the second are given a ḍamma’”."},
]
