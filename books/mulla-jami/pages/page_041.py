# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 41 (printed ٤٠)."""

PAGE_NUMBER = 41
PRINTED_PAGE = "٤٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "وقيد «الإفراد»[[١]] لإخراج المركبات مطلقا، سواء كانت كلامية أو غير كلامية.",
     "en": "He stipulated the restriction of “singularity” (ifrād) in order to exclude compounds absolutely, whether they be sentential (kalāmiyya) or non-sentential."},
    {"type": "matn",
     "ar": "فيخرج به عن حد الكلمة، مثل: «الرجل»[[٢]]، و«قائمة»، و«بصري»، وأمثالها مما يدل جزء اللفظ منه على جزء معناه،",
     "en": "By it there is excluded from the definition of the word (kalima) the likes of “al-rajul” (the man), “qāʾima,” and “baṣrī,” and their likes — in which a part of the utterance signifies a part of its meaning —"},
    {"type": "matn",
     "ar": "لكنه يعد[[٣]] لشدة الامتزاج لفظة واحدة، وأعرب بإعراب واحد[[٤]].",
     "en": "yet [each] is counted, on account of the intensity of fusion (imtizāj), as a single utterance (lafẓa wāḥida), and is inflected with a single inflection (iʿrāb)."},
    {"type": "matn",
     "ar": "ويبقى مثل: «عبد الله» علما داخلا فيه، مع أنه معرب بإعرابين[[٥]].",
     "en": "And the like of “ʿAbd Allāh” as a proper name remains included within it [the definition], even though it is inflected with two inflections."},
    {"type": "matn",
     "ar": "ولا يخفى[[٦]] على الفطن العارف بالغرض من علم النحو أنه لو كان الأمر بالعكس لكان أنسب.",
     "en": "It is not hidden from the astute one who knows the aim of the science of grammar (naḥw) that, had the matter been the reverse, it would have been more fitting."},
    {"type": "matn",
     "ar": "وما أورده صاحب المفصل في تعريف الكلمة حيث قال: «هي: اللفظة الدالة",
     "en": "And as for what the author of al-Mufaṣṣal [al-Zamakhsharī] adduced in defining the word, where he said: “It is the single utterance that signifies"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سواء كان صفة لمعنى أو للفظ، أو حالا عن أحدهما.",
     "en": "Whether it be an adjective of a meaning or of a word, or a circumstantial qualifier (ḥāl) of one of the two."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ومثل: «رجل» أيضا، فإن لام التعريف والتنوين من حروف المعاني اتفاقا.",
     "en": "And likewise “rajul” (a man) also, for the definite-article lām and nunation (tanwīn) are, by agreement, among the particles of meaning (ḥurūf al-maʿānī)."},
    {"type": "pair",
     "ar": "وأما تاء التأنيث المتحركة وألفاه وياء النسبة وعلامتا التثنية والجمع كـ«مسلمان ومسلمون»، فذهب الشيخ الرضي وجماعة إلى أنها أيضا من حروف المعاني.",
     "en": "As for the mobile tāʾ of feminization and its two alifs [of feminization], the yāʾ of relative attribution (nisba), and the two signs of the dual and plural — as in “muslimān” and “muslimūn” — Shaykh al-Raḍī and a group held that these too are among the particles of meaning."},
    {"type": "pair",
     "ar": "وذهب جماعة إلى أنها من حروف المباني، وجعلوا مجموع الصيغة دالا على المعنى المقصود، إلا أن تلك الدلالة لما كانت بزيادة تلك الحروف نسبت الدلالة إليها،",
     "en": "Another group held that they are among the particles of structure (ḥurūf al-mabānī), and made the whole form signify the intended meaning; except that, since that signification came about through the addition of those letters, the signification was attributed to them —"},
    {"type": "pair",
     "ar": "كما نسب الطلب إلى سين «استفعل» والمطاوعة إلى «نون» انفعل.",
     "en": "just as the [sense of] seeking (ṭalab) is attributed to the sīn of “istafʿala,” and [the sense of] passive-reflexivity (muṭāwaʿa) to the nūn of “infaʿala.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "من «عد» المتعدي إلى اثنين.",
     "en": "From “ʿadda” (to count/reckon), which is transitive to two objects."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "كأن المراد بالإعراب معنى يشمل الحركة الإعرابية والبنائية.",
     "en": "It is as though what is intended by “inflection” (iʿrāb) is a sense encompassing both the inflectional vowel and the structural vowel (al-ḥaraka al-iʿrābiyya wa-l-bināʾiyya)."},
    {"type": "pair",
     "ar": "والحاصل: أنه لم يعتبر لكل من الجزأين حاله اللائق، فإن الحرف الأخير في «قائمة» لم يستحق الإعراب، بل البناء، والمستحق للإعراب هو «قائم»، فجعل المجموع كلمة واحدة.",
     "en": "The upshot is: he did not take into account, for each of the two parts, its appropriate state; for the final letter in “qāʾima” does not merit inflection but rather indeclinability (bināʾ), while the one meriting inflection is “qāʾim” — so he treated the whole as a single word."},
    {"type": "pair",
     "ar": "ولا يخفى أن هذا ظاهر في «قائمة» و«بصري» و«حبلى» و«حمراء» دون «الرجل» و«رجل» والمثنى والجمع بالواو والنون، فإن المعرب في الأول ليس إلا الجزء الثاني، وفي الثاني الجزء الأول.",
     "en": "It is not hidden that this is evident in “qāʾima,” “baṣrī,” “ḥublā,” and “ḥamrāʾ,” but not in “al-rajul,” “rajul,” the dual, and the plural with wāw and nūn — for the inflected element in the first [group] is only the second part, and in the second [group] the first part."},
    {"type": "pair",
     "ar": "وكذا في الأخيرين، فإن علامة التثنية والجمع فيهما إعراب بالحقيقة، وفيه تأمل.",
     "en": "And likewise in the last two [the dual and the plural], for the sign of the dual and plural in them is in reality an inflection; and in this there is [room for] reflection (taʾammul)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إن قلت: ما توجيه الإعرابين لكلمة واحدة وتعدد الإعراب ليس إلا لتعدد المقتضي، ولا تعدد للمقتضي في كلمة واحدة في إطلاق واحد؟",
     "en": "If you say: what is the justification for two inflections in a single word, when the multiplicity of inflection is only due to the multiplicity of the governing requisite (muqtaḍī), and there is no multiplicity of the requisite in a single word under a single application (iṭlāq)?"},
    {"type": "pair",
     "ar": "قلنا: قد تعتبر في الأعلام الأحوال التي يقتضيها الوضع السابق، وهو باعتبار الوضع السابق كلمتان.",
     "en": "We say: In proper names, the states required by the prior positing may be taken into account, and [the name], by consideration of the prior positing, is two words."},
    {"type": "pair",
     "ar": "وقال صاحب اللباب: إن إعراب آخره محكي كما في: «تأبط شرا».",
     "en": "The author of al-Lubāb said: the inflection of its end is [merely] quotative/verbatim (maḥkī), as in “Taʾabbaṭa Sharran.”"},
    {"type": "pair",
     "ar": "ولما كان الآخر مشغولا، والأول فارغا أظهر إعرابه في الجزء الفارغ، كما أظهر إعراب ما بعد «غير» في الاستثناء في «الغير»، فليس لـ«عبد الله» علما إلا إعراب واحد.",
     "en": "And since the last part is occupied (mashghūl) and the first vacant (fārigh), he made its inflection apparent on the vacant part — just as the inflection of what comes after “ghayr” in exception (istithnāʾ) is made apparent on “al-ghayr” — so “ʿAbd Allāh” as a proper name has only a single inflection."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "اعلم أن الغرض من علم النحو معرفة أحوال اللفظ وتصحيح إعرابه، فإهمال جانب اللفظ والميل إلى جانب المعنى لا يلائم ذلك الغرض.",
     "en": "Know that the aim of the science of grammar (naḥw) is knowing the states of the word (lafẓ) and rectifying its inflection; hence neglecting the side of the word and inclining toward the side of the meaning does not suit that aim."},
    {"type": "pair",
     "ar": "ولا يخفى أن ذلك الإهمال لا يجري في كل ما يعد لشدة الامتزاج لفظة واحدة، بل فيما أعرب بإعراب الكلمة الواحدة.",
     "en": "And it is not hidden that this neglect does not apply to everything that is counted as a single utterance on account of intensity of fusion, but only to what is inflected with the inflection of a single word."},
]
