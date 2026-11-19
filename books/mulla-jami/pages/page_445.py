# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 445 (printed ٤٤٤)."""

PAGE_NUMBER = 445
PRINTED_PAGE = "٤٤٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «أي: يتعلق بها» at the foot of PDF p. 444 (mid-sentence).
    {"type": "matn",
     "ar": "القصد في ضمن ذلك الاسم (بحروف مفرده) أي: بحروف هي مادة لمفرده[[١]] الذي هو الاسم[[٢]] الدال على واحد واحد من تلك الآحاد",
     "en": "…the intention is directed within that noun, (by the letters of its singular), that is, by letters that are the material of its singular, which is the noun indicating each single one of those units,"},
    {"type": "matn",
     "ar": "حال كون تلك الحروف متلبسة (بتغير ما) بحسب الصورة، إما بزيادة أو نقصان أو اختلاف في الحركات والسكنات حقيقة أو حكما.",
     "en": "while those letters are accompanied (by some change) in form, whether by addition, reduction, or a difference in the vowels and quiescences, really or by status."},
    {"type": "matn",
     "ar": "فالجار في قوله: «بحروف مفرده» إما متعلق بقوله: «مقصودة»، أو بقوله: «دل»، أو بهما على سبيل التنازع،",
     "en": "So the preposition in his words “by the letters of its singular” is attached either to his word “intended”, or to his word “indicates”, or to both by way of contention (tanāzuʿ);"},
    {"type": "matn",
     "ar": "وقوله: «بتغير ما» ظرف مستقر حال من الحروف،",
     "en": "and his words “by some change” are a stable adverbial phrase (ẓarf mustaqarr) serving as a circumstantial qualifier (ḥāl) of “the letters”."},
    {"type": "matn",
     "ar": "ودخل في قوله: «بتغير ما» جمعا السلامة؛ لأن الواو والنون في آخر الاسم من تمامه. وكذا الألف والتاء، فتغيرت الكلمة بهذه الزيادات إلى صيغة أخرى،",
     "en": "Included in his words “by some change” are the two sound plurals, because the wāw and nūn at the end of the noun are part of its completion, and likewise the alif and tāʾ; so the word is changed by these additions into another form."},
    {"type": "matn",
     "ar": "وقوله: «ما دل على آحاد» جنس يشمل المجموع، وأسماء الأجناس[[٣]] كـ«تمر ونخل»، فإنها وإن لم تدل عليها[[٤]] وضعا فقد تدل عليها استعمالا،",
     "en": "His words “what indicates units” are a genus that includes the plural; generic nouns (asmāʾ al-ajnās), like “tamr” (dates) and “nakhl” (palms), for even if they do not indicate them by coinage (waḍʿ), they may indicate them in usage;"},
    {"type": "matn",
     "ar": "وأسماء الجموع كـ«رهط ونفر»، وبعض أسماء العدد كـ«ثلاثة وعشرة»،",
     "en": "collective nouns (asmāʾ al-jumūʿ), like “rahṭ” and “nafar” (a band of men); and some numerals, like “thalātha” (three) and “ʿashara” (ten)."},
    # REVIEW: printed «الإفراد» (kasra-form, “singularity”); context calls for «الأفراد» (“individuals”); transcribed as printed, translated as «الأفراد».
    {"type": "matn",
     "ar": "وبقوله: «مقصودة بحروف مفرده» خرجت أسماء الأجناس، فإذا قصد بها نفس الجنس لا أفراده فبقوله: «مقصودة»، وإذا قصد بها الإفراد استعمالا، فبقوله: «بحروف مفرده»،",
     "en": "By his words “intended by the letters of its singular” the generic nouns are excluded: when the genus itself is intended by them, not its individuals, then by his word “intended”; and when individuals are intended by them in usage, then by his words “by the letters of its singular”."},
    {"type": "matn",
     "ar": "وكذلك بقوله: «بحروف مفرده» خرجت أسماء الجموع والعدد.",
     "en": "Likewise by his words “by the letters of its singular” the collective nouns and the numerals are excluded."},
    {"type": "matn",
     "ar": "(فنحو: «تمر») مما هو الفارق بينه وبين واحده التاء (و) نحو: (ركب) مما هو اسم",
     "en": "(So the like of “tamr”), among those where what distinguishes it from its unit noun is the tāʾ, (and) the like of (“rakb”) (a company of riders), among those that are a…"},

    {"type": "rule"},

    # Continuation of footnote ٧ from PDF p. 444 (printed ٤٤٣).
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "والتاء من تمام الاسم.",
     "en": "…and the tāʾ are part of the completion of the noun."},
    # REVIEW: printed «حاملين»; the parallel matn on printed ٤٤٥ has «جامل» (camel herd), so «جاملين» may be intended; transcribed as printed.
    {"type": "pair",
     "ar": "والمراد بالدلالة المطابقة كما هو المتبادر، فلا يدخل مثنى اسم الجمع والجمع المكسر نحو: حاملين وجمالين،",
     "en": "What is meant by “indication” is correspondent indication (dalālat al-muṭābaqa), as first comes to mind; so the dual of a collective noun and of a broken plural, like “ḥāmilayn” [sic] and “jimālayn”, is not included;"},
    {"type": "pair",
     "ar": "فإنهما وإن دلتا على الآحاد، لكن لا بالمطابقة؛ إذ المدلول المطابقي لهما اثنان من الجماعة، وكل جماعة تشمل الآحاد، فالدلالة عليها تضمنية.",
     "en": "for although these two indicate units, it is not by correspondence, since what they correspondingly signify is two of the group, and each group comprises the units; so the indication of them is implicative (taḍammunī)."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "بيان وجه اختصاص الحروف بالمفرد المستفاد من اللام المقدرة.",
     "en": "[This is] a statement of the ground for the letters’ belonging specifically to the singular, which is conveyed by the implied lām."},
    {"type": "pair",
     "ar": "والمراد بالمفرد أعم من الحقيقي والتقديري كالجمع الذي لا مفرد له،",
     "en": "What is meant by “the singular” is more general than the real and the supposed, as with a plural that has no singular;"},
    {"type": "pair",
     "ar": "وزاد لفظ الحروف، ولم يقل: بمفرده، فإن حروف المفرد متحققة فيه، وإن لم يتحقق المفرد.",
     "en": "and he added the word “letters” and did not say “by its singular”, for the letters of the singular are realized in it even if the singular is not realized."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إشارة إلى أن المفرد ههنا وإن كان في مقابلة المثنى والمجموع لكن الملحوظ ههنا هذا المفهوم، وهو كونه دالا على واحد واحد، فلا دور في التعريف.",
     "en": "[This is] an indication that “the singular” here, although it stands opposite the dual and the plural, is considered here under this concept, namely its indicating each single one; so there is no circularity in the definition."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "التي يفرق بينها وبين واحدها بالتاء، فإنها للدلالة على الآحاد.",
     "en": "Those distinguished from their unit noun by the tāʾ, for they serve to indicate units."},
    {"type": "pair",
     "ar": "وأما التي لا فرق بينها وبين واحدها فإنها تدل على الماهية كالماء والتراب والعسل والخل.",
     "en": "As for those with no distinction between them and their unit, they indicate the quiddity, like water, earth, honey and vinegar."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فالمراد بالدلالة الدلالة في الجملة سواء كان وضعا فقط كما في الجمع المستعمل في الواحد نحو: شابت مفارقه، أو في الاثنين نحو: قلوبكما",
     "en": "So what is meant by “indication” is indication in some manner, whether by coinage only, as in a plural used for one, like “shābat mafāriquhu” (the partings of his hair turned grey), or for two, like “qulūbukumā” (your two hearts);"},
    {"type": "pair",
     "ar": "أو استعمالا فقط كما في أسماء الأجناس، أو وضعا واستعمالا كما في الجموع المستعملة في معانيها الحقيقية،",
     "en": "or by usage only, as in generic nouns; or by coinage and usage, as in plurals used in their real meanings."},
    {"type": "pair",
     "ar": "ولو أريد الدلالة وضعا كما في تعريف الفعل خرج أسماء الأجناس بقوله: على آحاد.",
     "en": "Had indication by coinage been meant, as in the definition of the verb, generic nouns would have been excluded by his words “units”."},
]
