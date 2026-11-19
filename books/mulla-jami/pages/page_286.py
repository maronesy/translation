# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 286 (printed ٢٨٥)."""

PAGE_NUMBER = 286
PRINTED_PAGE = "٢٨٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «ولا حكما إذا اكتفى بدخوله على المبدل» from the foot of PDF p. 285.
    {"type": "matn",
     "ar": "منه، واعتبر سراية حكمه إليه، فإنه في قوة التقدير حال كونهما (عاملتين) في المستثنى المحمول على البدل (بعده) أي: بعد الإثبات،",
     "en": "…and its effect is considered to extend to it, for that is equivalent to supposing [them]—(as governing) the excepted that is carried as a substitute (after it), that is, after the affirmation;"},
    {"type": "matn",
     "ar": "يعني: بعد ما صار الكلام مثبتا لانتقاض النفي بـ«إلا» (لأنهما) أي: «ما ولا» (عملتا للنفي[[١]]، وقد انتقض النفي بـ«إلا»)",
     "en": "meaning: after the sentence has become affirmative through the negation being broken by “illā”—(because they), that is, “mā” and “lā,” (govern by virtue of negation, and the negation has been broken by “illā”)."},
    {"type": "matn",
     "ar": "وحيث تعذر في هاتين الصورتين البدل على اللفظ حمل على المحل،",
     "en": "Since in these two cases the substitute on the wording is precluded, it is carried on the place (maḥall):"},
    {"type": "matn",
     "ar": "فـ«عمرو» مرفوع على أنه محمول على محل «أحد»، وهو الرفع بالابتداء، و«شيء» مرفوع على أنه محمول على محل «شيئا»، وهو الرفع بالخبرية.",
     "en": "“ʿAmr” is nominative as being carried on the place of “aḥad,” which is the nominative of inchoation (ibtidāʾ); and “shayʾ” is nominative as being carried on the place of “shayʾan,” which is the nominative of being a predicate (khabariyya)."},
    {"type": "matn",
     "ar": "فإن قلت: لـ«أحد» في هذا المثال محلان من الإعراب: محل قريب وهو نصبه بكلمة «لا»، ومحل بعيد وهو رفعه بالابتداء، فلم اعتبروا حمله على محله البعيد لا القريب؟",
     "en": "If you say: “aḥad” in this example has two inflectional places: a near place, which is its accusative by the word “lā,” and a remote place, which is its nominative by inchoation; so why did they consider carrying it on its remote place and not the near one?"},
    {"type": "matn",
     "ar": "قلت: لأن محله القريب إنما هو لعمل «لا» فيه بمعنى النفي، وقد انتقض النفي بـ«إلا» بخلاف محله البعيد، فإنه لا دخل لعمل «لا» فيه.",
     "en": "I say: because its near place is due solely to the government of “lā” in it by virtue of negation, and the negation has been broken by “illā”; unlike its remote place, in which the government of “lā” has no part."},
    {"type": "matn",
     "ar": "(بخلاف «ليس زيد شيئا إلا شيئا») مع أنه انتقض النفي فيه أيضا بـ«إلا» (لأنها) أي: «ليس» (عملت للفعلية) لا للنفي",
     "en": "(Unlike “Zayd is not anything except something [shayʾan]”), even though the negation in it too is broken by “illā”, (because it), that is, “laysa,” (governs by virtue of being a verb), not by virtue of negation;"},
    {"type": "matn",
     "ar": "(فلا أثر لنقض معنى النفي[[٢]]) في عملها (لبقاء الأمر العاملة هي) أي: «ليس» (لأجله) أي: لأجل ذلك الأمر، وهو الفعلية[[٣]].",
     "en": "(so the breaking of the sense of negation has no effect) on its government, (because the factor for whose sake it), that is, “laysa,” (governs remains), namely verbhood (fiʿliyya)."},
    {"type": "matn",
     "ar": "(ومن «ثمة») أي: ومن أجل أن عمل «ليس» للفعلية لا للنفي، وعمل «ما ولا» بالعكس",
     "en": "(And for that reason), that is, because the government of “laysa” is by virtue of verbhood, not negation, while the government of “mā” and “lā” is the reverse,"},
    {"type": "matn",
     "ar": "(جاز «ليس زيد إلا قائما») بإعمال «ليس» في «قائما» وإن انتقض نفيها بـ«إلا» لبقاء فعليتها",
     "en": "(“Zayd is nothing but standing [qāʾiman]” is permitted), with “laysa” governing “qāʾiman,” even though its negation is broken by “illā,” because its verbhood remains;"},
    {"type": "matn",
     "ar": "(وامتنع «ما زيد إلا قائما») بإعمال «ما» في «قائما»؛ لأن عملها فيه إنما هو للنفي، وقد انتقض النفي بـ«إلا».",
     "en": "(and “Mā Zaydun illā qāʾiman” is excluded), with “mā” governing “qāʾiman,” because its government in it is solely by virtue of negation, and the negation has been broken by “illā.”"},
    {"type": "matn",
     "ar": "(و) المستثنى (مخفوض) أي: مجرور (بعد «غير» و«سوى») مع كسر السين أو ضمها[[٤]] مع القصر (و«سواء») بفتح السين وكسرها مع المد، لكونه مضافا إليه",
     "en": "(And) the excepted is (in the genitive [makhfūḍ]), that is, majrūr, (after “ghayr” and “siwā”)—with kasra or ḍamma on the sīn, with the short ending—(and “sawāʾ”)—with fatḥa or kasra on the sīn, with the long ending—because it is the second term of a genitive construction (muḍāf ilayhi);"},
    {"type": "matn",
     "ar": "(وبعد",
     "en": "(and after…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يعني: أنه علة حملهما على ليس وإن أو جزء العلة. وعلى التقديرين بانتفائه تنتفي العلة.",
     "en": "Meaning: it is the cause of their being assimilated to “laysa” and “inna,” or part of the cause; and on either supposition, with its disappearance the cause disappears."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: انتقاضه، فهو مصدر مجهول.",
     "en": "That is, its being broken; so it is a verbal noun (maṣdar) of the passive."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وذلك لأن معنى ليس في الأصل «ما كان» بدليل لحوق علامات الأفعال عليه، نحو: ليست ولست،",
     "en": "That is because the meaning of “laysa” is originally “mā kāna” (was not), as shown by the attachment to it of the marks of verbs, as in “laysat” and “lastu”;"},
    {"type": "pair",
     "ar": "ثم سلبت الدلالة على الزمان الماضي، فحكمها حكم «ما كان»، وإن لم يبق فيه معنى الكون، وهو قد ينتفي نفيه ويبقى عمله، نحو: ما كان زيد إلا قائما، لبقاء معنى الكون بعد «إلا».",
     "en": "then it was stripped of the indication of past time; so its rule is the rule of “mā kāna,” even though the sense of being (kawn) does not remain in it; and the negation of that [mā kāna] may cease while its government remains, as in “Zayd was nothing but standing,” because the sense of being remains after “illā.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: كسر السين مع القصر، وفتحها مع المد مشهورتان.",
     "en": "Shaykh al-Raḍī said: kasra on the sīn with the short ending, and fatḥa with the long ending, are the two well-known [forms]."},
]
