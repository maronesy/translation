# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 180 (printed ١٧٩)."""

PAGE_NUMBER = 180
PRINTED_PAGE = "١٧٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "قولهم: «لا رجل في الدار» لاحتمال حذف الخبر، وجعل «في الدار» صفة[[١]]،",
     "en": "…their saying “There is no man in the house” (lā rajula fī al-dāri), because of the possibility that the predicate is elided and “in the house” is made an adjective—"},
    {"type": "matn",
     "ar": "بخلاف ما ذكر؛ لأن «غلام رجل» معرب منصوب لا يجوز ارتفاع صفته[[٢]] على ما هو الظاهر[[٣]]",
     "en": "unlike what has been mentioned; because “ghulāma rajulin” is declinable and accusative, and its adjective may not be nominative, according to what is apparent—"},
    {"type": "matn",
     "ar": "(فيها) أي: «في الدار» خبر بعد خبر لا ظرف «ظريف» ولا حال؛ لأن الظرافة لا تتقيد بالظرف ونحوه[[٤]]،",
     "en": "(in it): that is, “in the house” is a second predicate, not an adverbial qualifier of “ẓarīf,” nor a circumstantial (ḥāl); because cleverness is not restricted by an adverbial and the like."},
    {"type": "matn",
     "ar": "وإنما أتى به؛ لئلا يلزم الكذب بنفي ظرافة كل غلام رجل، وليكون مثالا لنوعي خبرها[[٥]] الظرف وغيره.",
     "en": "He brought it in only so that falsehood would not follow from negating the cleverness of every man’s servant, and so that it would be an example of both kinds of its predicate—the adverbial and the other."},
    {"type": "matn",
     "ar": "(ويحذف) خبر «لا» هذه حذفا (كثيرا[[٦]]) إذا كان الخبر عاما كـ«الموجود والحاصل» لدلالة النفي عليه[[٧]]،",
     "en": "(And it is elided)—the predicate of this “lā”—with an elision [that is] (frequent), when the predicate is general, like “existent” and “obtaining,” because the negation indicates it;"},
    {"type": "matn",
     "ar": "نحو: «لا إله إلا الله» أي: «لا إله موجود إلا الله».",
     "en": "as in: “There is no god but Allah” (lā ilāha illā Allāh), that is: “There is no god existent but Allah.”"},
    {"type": "matn",
     "ar": "(وبنو تميم لا يثبتونه) أي: لا يظهرون الخبر في اللفظ؛ لأن الحذف عندهم واجب،",
     "en": "(And the Banū Tamīm do not state it); that is, they do not make the predicate overt in the utterance, because for them the elision is obligatory."},
    {"type": "matn",
     "ar": "أو المراد أنهم لا يثبتونه أصلا لا لفظا ولا تقديرا، فيقولون معنى قولهم: «لا أهل ولا مال»: «انتفى الأهل والمال»، فلا يحتاج إلى تقدير الخبر،",
     "en": "Or what is meant is that they do not posit it at all, neither in utterance nor by supposition (taqdīr); so they say the meaning of their saying “No family and no wealth” (lā ahla wa-lā māla) is “Family and wealth have ceased to be,” and there is no need to supply a predicate."},
    {"type": "matn",
     "ar": "وعلى التقديرين يحملون ما يرى خبرا في مثل: «لا رجل قائم» على الصفة دون الخبر.",
     "en": "On both interpretations they construe what appears to be a predicate in such as “No man is standing” (lā rajula qāʾimun) as an adjective, not as a predicate."},

    {"type": "section", "ar": "[ اسم ما ولا المشبهتين بليس ]",
     "en": "The Noun of “Mā” and “Lā” Resembling “Laysa”"},

    {"type": "matn",
     "ar": "(اسم «ما» و«لا» المشبهتين بـ«ليس») في معنى النفي، والدخول على المبتدأ",
     "en": "(The noun of “mā” and “lā” that resemble “laysa”) in the meaning of negation and in entering upon the subject…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قال المصنف: المثال الحسن ما يكون واضحا غير محتمل؛ لأنه للإيضاح فحقه أن يستغني عن الإيضاح،",
     "en": "The author said: a good example is one that is clear and not open to [other] possibilities; because it is for clarification, so it ought to need no clarification [itself]."},
    {"type": "pair",
     "ar": "وكما أن في الدار في \"لا رجل في الدار\" يحتمل أن يكون صفة «رجل» يحتمل ذلك في «لا غلام رجل»، فلذلك عدل عن جزئي المثال.",
     "en": "And just as “in the house” in “lā rajula fī al-dāri” may be an adjective of “rajul,” that is possible in “lā ghulāma rajulin” [as well]; for that reason he departed from both parts of the example."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "هكذا قال المصنف. واعترض عليه بأنه يجوز عند جماعة.",
     "en": "So the author said. It was objected against him that it is permissible according to a group [of grammarians]."},
    {"type": "pair",
     "ar": "فزاد الشارح لدفعه قوله: «على ما هو الظاهر»، يعني أن رفع صفة المعرب المنصوب خلاف الظاهر،",
     "en": "So the commentator added, to ward it off, his words “according to what is apparent”—meaning that putting the adjective of a declinable accusative noun in the nominative is contrary to what is apparent."},
    {"type": "pair",
     "ar": "فالاحتمال الظاهر في «لا غلام رجل ظريف» الخبرية دون الوصفية. وهذا يكفي لوضوح المثال وحسنه.",
     "en": "So the apparent possibility in “lā ghulāma rajulin ẓarīfun” is that it is a predicate, not an adjective; and this suffices for the clarity and goodness of the example."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إنما قال ذلك لجواز ارتفاع صفته حملا على المحل، كما ذهب إليه جماعة.",
     "en": "He said that only because its adjective may be nominative by construing it with the [syntactic] position, as a group [of grammarians] held."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "من الحال بدون سماحة.",
     "en": "[Such as] the circumstantial (ḥāl), without looseness."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وليكون مثالا للخبر المتعدد، فإنه أحوج إلى الإيضاح، فلو ترك بيان نوعي الخبر لكان أشمل.",
     "en": "And so that it would be an example of the multiple predicate, for that is more in need of clarification; had he left aside specifying the two kinds of predicate, it would have been more comprehensive."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "قدر موصوفا كثيرا مصدرا لفعل،",
     "en": "He supplied, as the qualified noun of “kathīran,” a verbal noun (maṣdar) of the verb;"},
    {"type": "pair",
     "ar": "والمشتهر في مثله تقدير الزمان، وهو الملائم لقوله: وبنو تميم لا يثبتونه أصلا.",
     "en": "but what is well known in such a case is supplying [a noun of] time, and that is what accords with his words: “and the Banū Tamīm do not state it at all.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "يقال: لأن النفي يقتضي منفيا. ولما لم يكن قرينة خصوص ينصرف إلى العام.",
     "en": "It is said: because negation requires something negated; and since there is no indicator of a specific [predicate], it is taken to refer to the general one."},
    {"type": "pair",
     "ar": "وقيل: لأن النفي رفع الوجود. ورد بأن النفي رفع الوجود الشامل للوجود في نفسه، وللوجود لغيره، فلا يدل على الوجود في نفسه،",
     "en": "It has also been said: because negation is the removal of existence. This was rejected on the grounds that negation is the removal of existence in the sense that includes existence in itself and existence for another, so it does not indicate existence in itself."},
    {"type": "pair",
     "ar": "وهو ليس بشيء؛ لأن المتبادر من النفي نفي الوجود في نفسه، كما أن المتبادر من الوجود الوجود في نفسه، فينصرف عن الإطلاق إلى نفي الوجود في نفسه.",
     "en": "That [rejection] is of no account, because what first comes to mind from negation is the negation of existence in itself, just as what first comes to mind from existence is existence in itself; so, when unqualified, it is taken to refer to the negation of existence in itself."},
]
