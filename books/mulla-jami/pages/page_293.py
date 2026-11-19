# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 293 (printed ٢٩٢)."""

PAGE_NUMBER = 293
PRINTED_PAGE = "٢٩٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… خرج به مثل: «أبوه» في «لا غلام رجل أبوه قائم» لما» from the foot of PDF p. 292.
    {"type": "matn",
     "ar": "عرفت[[١]]، وهذا القدر كاف[[٢]] في حد اسمها مطلقا؛",
     "en": "…you have learned; and this much suffices for the definition of its noun absolutely;"},
    {"type": "matn",
     "ar": "لكنه لما أراد حد المنصوب منه زاد عليه قوله: (يليها) أي: يلي المسند إليه لفظة «لا»، أي: يقع بعدها بلا فاصلة",
     "en": "but since he wished to define the accusative part of it, he added to it his words (it follows it), that is, that to which [something] is predicated follows the word “lā,” that is, it occurs after it with no separation,"},
    {"type": "matn",
     "ar": "(نكرة مضافا أو مشابها به) أي: بالمضاف في تعلقه بشيء هو من تمام معناه،",
     "en": "(being indefinite, annexed or resembling it), that is, resembling the annexed noun (muḍāf) in its being attached to something that completes its meaning."},
    {"type": "matn",
     "ar": "وهذه أحوال مترادفة من الضمير المجرور في «إليه» أو في الأولى منه، أو من الضمير المجرور في «دخولها» وما بقي من الضمير المرفوع في «يليها»",
     "en": "These are consecutive circumstantial qualifiers (aḥwāl mutarādifa) of the genitive pronoun in “ilayhi,” or [are such] in the first of them; or of the genitive pronoun in “dukhūlihā,” with the rest being of the nominative pronoun in “yalīhā.”"},
    {"type": "matn",
     "ar": "(مثل: «لا غلام رجل») مثال لما يليها نكرة مضافا.",
     "en": "(As in “lā ghulāma rajulin” [there is no slave of a man]) is an example of what follows it being indefinite and annexed."},
    {"type": "matn",
     "ar": "وفي بعض النسخ: «لا غلام رجل ظريف فيها»، وقد عرفت في المرفوعات تحقيق قوله فيها.",
     "en": "In some copies: “There is no slave of a man, refined, in it”; and you have already learned, in [the chapter on] the nominatives, the verification of his saying “fīhā” (in it)."},
    {"type": "matn",
     "ar": "(و«لا عشرين درهما لك») مثال لما يليها نكرة مشبها بالمضاف،",
     "en": "(And “lā ʿishrīna dirhaman laka” [you have no twenty dirhams]) is an example of what follows it being indefinite and resembling the annexed noun;"},
    {"type": "matn",
     "ar": "وقوله: «لك» على النسخ المشهورة من تتمة المثالين كليهما[[٣]].",
     "en": "and his word “laka” (for you), according to the well-known copies, completes both examples."},
    {"type": "matn",
     "ar": "(فإن كان) أي: المسند إليه بعد دخولها[[٤]] غير واقع على الأحوال المذكورة، بل كان (مفردا) بانتفاء الشرط الأخير فقط، وهو كونه مضافا أو مشبها به،",
     "en": "(If it is), that is, if that to which [something] is predicated after its entry does not occur in the states mentioned, but is (single [mufrad]), through the absence of the last condition only, namely its being annexed or resembling the annexed,"},
    {"type": "matn",
     "ar": "أي: يليها نكرة غير مضاف ولا مشبه به، ليترتب عليه قوله: (فهو مبني على ما ينصب به)",
     "en": "that is, it follows it as an indefinite that is neither annexed nor resembling the annexed—so that his words (then it is indeclinable on that by which it is put in the accusative) may follow from it;"},
    {"type": "matn",
     "ar": "فإنه لو كان مفردا معرفة أو مفصولا بينه وبين «لا»، فحكمه غير ذلك.",
     "en": "for were it a single definite noun, or separated from “lā,” its rule would be otherwise."},
    {"type": "matn",
     "ar": "وقوله: «على ما ينصب به» أي: على ما كان ينصب به المفرد قبل دخول «لا» عليه",
     "en": "His words “on that by which it is put in the accusative” mean: on that by which the single noun was put in the accusative before the entry of “lā” upon it;"},
    {"type": "matn",
     "ar": "وهو الفتح في المفرد نحو: «لا رجل في الدار»، والكسر في جمع المؤنث السالم[[٥]] بلا تنوين[[٦]] نحو: «لا مسلمات في الدار»،",
     "en": "this is the fatḥa in the singular, as in “lā rajula fī l-dār” (there is no man in the house); the kasra without nunation (tanwīn) in the sound feminine plural, as in “lā muslimāti fī l-dār” (there are no Muslim women in the house);"},
    {"type": "matn",
     "ar": "والياء المفتوح ما قبلها في المثنى، والمكسور",
     "en": "and the yāʾ preceded by a fatḥa in the dual, and [the yāʾ] preceded by a kasra…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "من معنى البعدية أو الدخول.",
     "en": "[That is, what you have learned] of the meaning of “after” or of “entry.”"},
    {"type": "pair",
     "ar": "لا يخفى أنه لا حاجة في إخراجه عن تعريف المنصوب بلا إلى هذا؛ لأنه يخرج بقوله: يليها.",
     "en": "It is evident that there is no need for this in order to exclude it from the definition of what is put in the accusative by lā, since it is excluded by his words “it follows it.”"},
    {"type": "pair",
     "ar": "نعم، إنما الحاجة إليه في تعريف اسم لا.",
     "en": "Yes; the need for it is only in the definition of the noun of lā."},
    {"type": "pair",
     "ar": "ولعله قال ذلك ليصح قوله: وهذا القدر كاف في حد اسمها.",
     "en": "Perhaps he said that so that his statement “and this much suffices for the definition of its noun” would be sound."},
    {"type": "pair",
     "ar": "وقيل في إخراجه: المراد الذي أسند إليه خبرها.",
     "en": "It has been said about its exclusion: what is meant is that to which its predicate (khabar) is attributed."},
    {"type": "pair",
     "ar": "وعليه ما ذكرناه مع حذف مفعول ما لم يسم فاعله، واستدراك بعد دخولها.",
     "en": "Against this is what we have mentioned, together with the elision of the subject of the passive verb (mafʿūl mā lam yusamma fāʿiluhu), and the redundancy of “after its entry.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فيه أن المرفوع بعدها معرفة كان أو نكرة لا يسمى اسما لها، فالتعريف غير مانع،",
     "en": "Against this: the nominative noun after it, whether definite or indefinite, is not called its noun; so the definition is not exclusive (ghayr māniʿ)—"},
    {"type": "pair",
     "ar": "اللهم إلا أن يعنى: بالدخول عليه العمل فيه.",
     "en": "unless, that is, by “entry upon it” is meant “governing it.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هذا بعيد جدا؛ إذ لا يقال: لا غلام رجل لك، بل لا غلام لك،",
     "en": "This is very far-fetched, since one does not say “lā ghulāma rajulin laka” but rather “lā ghulāma laka” (you have no slave);"},
    {"type": "pair",
     "ar": "فالأولى أنه قصد في المثالين حذف خبر لا.",
     "en": "so it is preferable [to hold] that in the two examples he intended the elision of the predicate of lā."},
    {"type": "pair",
     "ar": "وذكره على طبق ما سبق أنه يحذف كثيرا، ولذا قدم مثال الحذف.",
     "en": "He mentioned it in keeping with what preceded, that it is often elided; for this reason he put the example with elision first."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يعني: أن ضمير «كان» راجع إليه لا إلى المنصوب كما يتوهم ولا إلى اسم «لا» المفعول ضمنا كما قيل لأن ذلك أظهر.",
     "en": "He means: the pronoun of “kāna” refers to it, not to “the accusative,” as one might imagine, nor to “the noun of lā,” understood implicitly, as has been said; because that is more evident."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "خلافا للمازني، فإنه يبنيه على الفتح.",
     "en": "Contrary to al-Māzinī, for he makes it indeclinable on the fatḥa."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لأنه وإن لم يكن للتمكن، لكنه مشابه له، فمنع من الدخول على المبني.",
     "en": "Because, although it is not [the nunation] of full declinability (tamakkun), it resembles it, and so it was barred from entering upon the indeclinable."},
    # REVIEW: print shows a stray hamza between «إلى» and «أن» («إلىءأن»), apparently a typesetting slip; transcribed as «إلى أن».
    {"type": "pair",
     "ar": "ومنهم من يبنيه على الكسر مع التنوين قياسا لا سماعا نظرا إلى أن التنوين للمقابلة.",
     "en": "Some make it indeclinable on the kasra with nunation, by analogy (qiyās), not by attested usage (samāʿ), considering that the nunation is that of correspondence (tanwīn al-muqābala)."},
]
