# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 81 (printed ٨٠)."""

PAGE_NUMBER = 81
PRINTED_PAGE = "٨٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "الياء في التثنية، لخفة الفتحة وكثرة التثنية، وكسروه في المجموع لثقل الكسرة وقلة المجموع،",
     "en": "... the yāʾ in the dual — on account of the lightness of the fatḥa and the frequency of the dual — and they gave it a kasra in the plural, on account of the heaviness of the kasra and the rarity of the plural;"},
    {"type": "matn",
     "ar": "وحملوا النصب على الجر، لا على الرفع لمناسبة النصب الجر، لوقوع كل منهما[[١]] فضلة في الكلام.",
     "en": "and they carried the accusative upon the genitive — not upon the nominative — because of the affinity of the accusative with the genitive, since each of the two occurs as a surplus element (faḍla) in speech."},

    {"type": "section",
     "ar": "[ الإعراب التقديري واللفظي ]",
     "en": "Estimated (Taqdīrī) and Pronounced (Lafẓī) Inflection"},

    {"type": "matn",
     "ar": "ولما فرغ من تقسيم الإعراب إلى الحركة والحرف[[٢]]، وبيان مواضعهما[[٣]] المختلفة، شرع في بيان مواضع الإعراب اللفظي والتقديري اللذين أشير إلى تقسيمه[[٤]] إليهما[[٥]] فيما سبق.",
     "en": "When he had finished dividing inflection into [inflection by] the vowel and the letter, and clarifying their differing loci, he embarked upon clarifying the loci of pronounced (lafẓī) and estimated (taqdīrī) inflection — the two [categories] into which its division was alluded to earlier."},
    {"type": "matn",
     "ar": "ولما كان التقديري أقل، أشار إليه أولا، ثم بين أن اللفظي ما عداه، فقال:",
     "en": "Since the estimated is the lesser [in occurrence], he pointed to it first, then made clear that the pronounced is what lies outside it. So he said:"},
    {"type": "matn",
     "ar": "(التقدير) أي: تقدير الإعراب (فيما) أي: في الاسم المعرب الذي (تعذر الإعراب فيه)[[٦]]، أي: امتنع ظهوره في لفظه،",
     "en": "(Estimation [al-taqdīr]) — that is, the estimating of inflection — (in that which) — that is, in the declinable noun in which (inflection is precluded [taʿadhdhara]) — that is, its manifestation in its wording is prevented;"},
    {"type": "matn",
     "ar": "وذلك إذا لم يكن الحرف الذي هو محل الإعراب قابلا للحركة الإعرابية، كما في الاسم المعرب بالحركة، الذي في آخره[[٧]] ألف مقصورة[[٨]]،",
     "en": "and that is when the letter which is the locus of inflection is not receptive to the inflectional vowel, as in a noun inflected by vowel whose ending is a shortened alif (alif maqṣūra),"},
    {"type": "matn",
     "ar": "سواء كانت موجودة في اللفظ كـ«العصا» بلام التعريف، أو محذوفة بالتقاء الساكنين (كعصا)[[٩]] بالتنوين، فإن الألف المقصورة في الصورتين غير قابلة للحركة.",
     "en": "whether it is present in the utterance, as in “al-ʿaṣā” (the staff) with the definite article, or elided through the meeting of two quiescents, as in “ʿaṣan” with nunation (tanwīn) — for the shortened alif in both cases is not receptive to a vowel."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: من النصب والجر، أي: ما فيه أحدهما.",
     "en": "That is: of the accusative and the genitive — i.e., that in which one of the two [occurs]."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: قوله «فالمفرد المنصرف والجمع المكسر المنصرف» إلى ههنا إشارة إلى تقسيم الإعراب إلى الإعراب بالحركة والإعراب بالحروف،",
     "en": "He means: his statement “the fully-declinable singular and the fully-declinable broken plural,” up to this point, is an allusion to the division of inflection into inflection by vowel and inflection by letters,"},
    {"type": "pair",
     "ar": "وبيان مواضعهما المختلفة في أنهما في بعض المواضع بالحركات الثلاث أو بالحروف الثلاثة، وفي بعض المواضع بالحركتين أو الحرفين.",
     "en": "and to the clarification of their differing loci — namely, that in some positions they [take] the three vowels or the three letters, and in some positions [only] two vowels or two letters."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "مواضع الإعراب بالحركة ومواضع الإعراب بالحروف.",
     "en": "The loci of inflection by vowel and the loci of inflection by letters."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: تقسيم الإعراب.",
     "en": "That is: the division of inflection."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: إلى اللفظي والتقديري.",
     "en": "That is: into the pronounced and the estimated."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "ففيه حذف العائد، والضمير المستتر راجع إلى الإعراب.",
     "en": "In it there is the omission of the referential pronoun (ʿāʾid), and the concealed pronoun refers back to “inflection.”"},
    {"type": "pair",
     "ar": "ولك أن تقول: الذي تعذر إعرابه، فحذف المضاف، وأقيم المضاف إليه مقامه، أعني: الضمير، فصار مرفوعا مستترا في الفعل.",
     "en": "You may also say: “that whose inflection is precluded,” whereby the annexed noun (muḍāf) is omitted and the noun to which it was annexed is set in its place — I mean the pronoun — so it becomes a concealed nominative [pronoun] within the verb."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: في موضع آخره فلا يلزم اتحاد الظرف والمظروف. ولك أن تقول: إن آخر الاسم عام، والألف خاص فلا يلزم الاتحاد.",
     "en": "That is: in the position of its end, so that the identity of container and contained (ẓarf and maẓrūf) is not entailed. You may also say: the end of the noun is general while the alif is specific, so their identity is not entailed."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "سميت بها؛ لأنها ضد الممدودة، أو لأنها ممنوعة من الحركات مطلقا، والقصر المنع، والأول أولى بدليل مقابلتها للممدودة، وعدم اختصاص المنع بالألف لتحققه في ميم غلامي.",
     "en": "It was so named either because it is the opposite of the extended [alif] (mamdūda), or because it is [entirely] prevented (mamnūʿa) from vowels — “qaṣr” meaning prevention. The first [meaning] is preferable, by the evidence of its being set against the “extended,” and because prevention is not exclusive to the alif, since it is realized [also] in the mīm of “ghulāmī.”"},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "وهي في حكم الثابت، ولهذا لم يعرب ما قبل الألف. ولخفاء أمر هذا القسم وظهور مقابله مثل بالأول وترك الثاني.",
     "en": "It [the elided alif] is in the ruling of the established [i.e., treated as though present], and for this reason what precedes the alif is not inflected. And because the matter of this category is obscure while its counterpart is manifest, he gave an example of the first and left out the second."},
]
