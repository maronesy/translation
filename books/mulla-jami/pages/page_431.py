# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 431 (printed ٤٣٠)."""

PAGE_NUMBER = 431
PRINTED_PAGE = "٤٣٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Begins a new sentence after «فاعتبر إفراده ليكون الفضلة قليلا.» at the foot of PDF p. 430.
    {"type": "matn",
     "ar": "(ومميز «مائة» و«ألف» و) مميز (تثنيتهما و) مميز (جمعه) أي: جمع الألف،",
     "en": "(The specifier of “miʾa” and “alf”, and) the specifier of (their dual, and) the specifier of (its plural), that is, the plural of alf:"},
    {"type": "matn",
     "ar": "وإنما لم يقل: «وجمعهما» كما قال: «وتثنيتهما»؛ لأن استعمال جمع «مائة» مع مميزها في الأعداد مرفوض،",
     "en": "he did not say “and their plural” as he said “and their dual” only because using the plural of “miʾa” with its specifier in numbers is rejected;"},
    {"type": "matn",
     "ar": "فلا يقال: «ثلاث مئات رجل» كما يقال: «ثلاثة آلاف رجل»[[١]] بخلاف التثنية، فإنه يقال: «مائتا رجل» مثل «ألفا رجل»",
     "en": "so one does not say “thalāth miʾāt rajul” as one says “thalāthat ālāf rajul” (three thousand men); unlike the dual, for one says “miʾatā rajul” (two hundred men) like “alfā rajul” (two thousand men)."},
    {"type": "matn",
     "ar": "(مخفوض مفرد[[٢]])؛ لأنه لما كانت «مائة» و«ألف» من أصول الأعداد كالآحاد، ناسب أن يكون مميزهما على طبق مميزها،",
     "en": "(is in the oblique case and singular); because, since “miʾa” and “alf” are among the base numbers like the units, it was fitting that their specifier should accord with the specifier of [the units];"},
    {"type": "matn",
     "ar": "لكنه لما كانت الآحاد في جانب القلة من الأعداد، و«المائة والألف» في جانب الكثرة منها،",
     "en": "but since the units are on the side of paucity among the numbers, and “hundred and thousand” on the side of multitude,"},
    {"type": "matn",
     "ar": "اختير في مميزها الجمع الموضوع للكثرة، وفي مميزهما المفرد الدال على القلة رعاية للتعادل.",
     "en": "the plural, which is coined for multitude, was chosen for the specifier of [the units], and the singular, which indicates paucity, for the specifier of [hundred and thousand], to maintain balance."},
    {"type": "matn",
     "ar": "(وإذا كان[[٣]] المعدود[[٤]] مؤنثا واللفظ) المعبر به عنه (مذكرا) كلفظ الشخص إذا عبرت بها عن المؤنث",
     "en": "(If the thing counted is feminine and the word) by which it is expressed (masculine), like the word shakhṣ (person) when you express a female by it,"},
    {"type": "matn",
     "ar": "(أو بالعكس) بأن يكون المعدود مذكرا، واللفظ مؤنثا، كلفظة \"النفس\" إذا عبرت بها عن المذكر",
     "en": "(or the reverse), that is, the thing counted is masculine and the word feminine, like the word “nafs” (soul) when you express a male by it,"},
    {"type": "matn",
     "ar": "(فوجهان) أي: ففي العدد وجهان: التذكير والتأنيث،",
     "en": "(then there are two options), that is, in the number there are two options: masculine and feminine."},
    {"type": "matn",
     "ar": "فإن شئت قلت: ثلاثة أشخص وأنت تريد النساء اعتبارا باللفظ، وهو الأكثر في كلامهم، وإن شئت قلت: ثلاث أشخص اعتبارا بالمعنى.",
     "en": "If you wish, you say “thalāthat ashkhuṣ” while meaning women, with regard to the word, and this is more frequent in their speech; and if you wish, you say “thalāth ashkhuṣ”, with regard to the meaning."},
    {"type": "matn",
     "ar": "(ولا يميز واحد) وواحدة (ولا اثنان) واثنتان وثنتان بمميز[[٥]]،",
     "en": "(Wāḥid) and wāḥida (is not specified, nor ithnān), ithnatān and thintān, by any specifier;"},
    {"type": "matn",
     "ar": "فلا يورد الواحد مع مميزه كما يقال: واحد رجل، ولا اثنان معه كما يقال: اثنا رجلين، بل يذكرون ما",
     "en": "so wāḥid is not brought with its specifier, as one might say “wāḥid rajul”, nor ithnān with it, as one might say “ithnā rajulayn”; rather they mention what…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "هذا الوجه إنما يتم لو لم يجز مئات رجل من غير إضافة عدد إليها، لكنه جاء مئات رجل.",
     "en": "This reasoning holds only if “miʾāt rajul” were not permissible without a number annexed to it; but “miʾāt rajul” is attested."},
    # REVIEW: «مآت» is printed here (elsewhere «مئات»); transcribed as printed.
    {"type": "pair",
     "ar": "قال الرضي: وإن لم يكن مآت مضافا إليها ثلاث وأخواته جمعت وأضيفت إلى المفرد أيضا نحو: مئات رجل.",
     "en": "Al-Raḍī said: even if miʾāt does not have thalāth and its sisters annexed to it, it is [still] pluralized and annexed to the singular, as in “miʾāt rajul”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قد يجمع نحو: مائة رجال، وقد يفرد منصوبا.",
     "en": "It is sometimes plural, as in “miʾat rijāl”, and sometimes singular in the accusative."},
    # REVIEW: the verse ends «والضاءة» as printed (the line is usually cited with «والفتاء»); transcribed as printed.
    {"type": "pair",
     "ar": "قال: إذا عاش الفتى مائتين عاما، فقد ذهب اللذاذة والضاءة.",
     "en": "[The poet] said: “When a young man lives two hundred years, delight and [radiance] are gone.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: هذا الاستعمال المفهوم مما تقدم من إثبات التاء في المذكر، وإسقاطها في المؤنث في ثلاثة إلى عشرة إذا كان المعدود ولفظه متفقين في التذكير والتأنيث،",
     "en": "That is: this usage understood from what preceded, of keeping the tāʾ for the masculine and dropping it for the feminine in three to ten, applies when the thing counted and its word agree in masculine and feminine gender;"},
    {"type": "pair",
     "ar": "وإذا كانا مختلفين فيهما فالوجهان، فكان الأليق تقديمه على بيان أحوال المميز",
     "en": "and when they differ in it, there are the two options. It would have been more fitting to put this before the explanation of the states of the specifier;"},
    {"type": "pair",
     "ar": "إلا أن تذكير لفظ المعدود وتأنيثه لما لم يعلم من المميز قدم ذكر المميز.",
     "en": "but since the masculine or feminine gender of the word for the thing counted is known only from the specifier, he put the mention of the specifier first."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سواء وقع تمييزا كما في مثال الشارح أو موصوفا نحو: الشخص ثلاثة أو ثلاث،",
     "en": "Whether it occurs as a specifier, as in the commentator’s example, or as a qualified noun, as in “al-shakhṣ thalātha” or “thalāth”."},
    {"type": "pair",
     "ar": "ولا ينتقض هذا الضابط بثلاث مائة، ولا العكس بثلاثة آلاف حيث وجب التذكير في الأول، والتأنيث في الثاني سواء كان المعدود مذكرا أو مؤنثا؛",
     "en": "This rule is not broken by “thalāth miʾa”, nor the reverse by “thalāthat ālāf”, where the masculine is obligatory in the first and the feminine in the second, whether the thing counted is masculine or feminine;"},
    {"type": "pair",
     "ar": "لأن التذكير فيهما بواسطة لفظ المائة والألف كما عرفت، ولم يعبر بهما عن المعدود، بل التعبير بلفظ مميزهما أعني: رجلا وامرأة مثلا.",
     "en": "because the gender in both is by means of the words miʾa and alf, as you know, and these are not used to express the thing counted; rather it is expressed by the word of their specifier, I mean, “man” and “woman”, for example."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "زاده للتنصيص على استغراق النفي، فإن الفعل المنفي ظاهر في العموم بخلاف النكرة في سياق النفي، فإنها نص فيه",
     "en": "He added it to state explicitly that the negation is all-inclusive; for the negated verb is apparent (ẓāhir) in generality, unlike an indefinite noun in a negative context, which is explicit (naṣṣ) in it."},
    {"type": "pair",
     "ar": "أي: لا يميز بمميز أصلا مفردا كان أو مثنى أو مجموعا.",
     "en": "That is, it is not specified by any specifier at all, whether singular, dual or plural."},
]
