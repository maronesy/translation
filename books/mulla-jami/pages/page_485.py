# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 485 (printed ٤٨٤)."""

PAGE_NUMBER = 485
PRINTED_PAGE = "٤٨٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(المضارع ما أشبه) أي: فعل أشبه (الاسم بأحد حروف «نأيت») أي: حال» at the foot of PDF p. 484 (mid-sentence).
    {"type": "matn",
     "ar": "كونه[[١]] متلبسا بأحد حروف «أتين»[[٢]] في أوائله[[٣]]، يعني: الحروف التي جمعتها كلمة «نأيت»[[٤]].",
     "en": "…while it is accompanied by one of the letters of “atayna” at its beginnings, meaning: the letters that the word “naʾaytu” gathers together."},
    {"type": "matn",
     "ar": "وهذه المشابهة إنما تكون (لوقوعه) أي: وقوع ذلك الفعل (مشتركا) بين زماني الحال والاستقبال على الصحيح، كوقوع الاسم مشتركا بين المعاني المتعددة كـ«العين».",
     "en": "This resemblance holds only (because of its occurring), that is, that verb’s occurring, (as shared) between the two times of the present and the future, according to the sound view, just as a noun occurs shared among several meanings, like “al-ʿayn”."},
    {"type": "matn",
     "ar": "(وتخصيصه) بالجر عطف على قوله: «وقوعه»، أي: وتلك المشابهة إنما تكون لوقوع الفعل مشتركا، ولتخصيصه[[٥]] بواحد من زماني الحال والاستقبال.",
     "en": "(And its being specified), in the genitive, coordinated with his words “its occurring”; that is, that resemblance holds only because of the verb’s occurring as shared, and because of its being specified to one of the two times of the present and the future"},
    {"type": "matn",
     "ar": "(بـ«السين») فإنه للاستقبال القريب (و«سوف»)، فإنه للاستقبال البعيد كما مر، كما أن الاسم يخصص بأحد معانيه بواسطة القرائن[[٦]].",
     "en": "(by “sa-”), which is for the near future, (and “sawfa”), which is for the distant future, as has passed; just as a noun is specified to one of its meanings by means of contextual indications (qarāʾin)."},
    {"type": "matn",
     "ar": "وإنما عرف المضارع بمشابهته الاسم؛ لأنه لم يسم مضارعا، إلا بهذا المعنى؛",
     "en": "He defined the muḍāriʿ (imperfect verb) by its resembling the noun only because it was named muḍāriʿ only in this sense;"},
    {"type": "matn",
     "ar": "إذ معنى المضارعة في اللغة: «المشابهة» مشتقة من «الضرع»، كأن كلا الشبيهين ارتضعا من ضرع واحد، فهما أخوان رضاعا.",
     "en": "for the meaning of muḍāraʿa in the language is “resemblance”, derived from “al-ḍarʿ” (the udder), as though both of the two resembling things had suckled from one udder, so that they are foster brothers."},
    {"type": "matn",
     "ar": "(فالهمزة[[٧]]) من تلك الحروف الأربعة (للمتكلم مفردا) مذكرا كان أو مؤنثا مثل: «أضرب».",
     "en": "(So the hamza), of those four letters, (is for the speaker alone), whether masculine or feminine, as in “aḍribu” (I strike)."},
    {"type": "matn",
     "ar": "(والنون له) أي: للمتكلم المفرد، إذا كان (مع غيره) واحدا كان ذلك الغير أو أكثر[[٨]]، مثل: «نضرب»، وكأنهما مأخوذان من «أنا» و«نحن».",
     "en": "(And the nūn is for him), that is, for the single speaker, when he is (with another), whether that other is one or more, as in “naḍribu” (we strike); it is as though the two were taken from “anā” (I) and “naḥnu” (we)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: printed «إذ لبس الحروف مشابها بها» (لبس); the sense expected is «ليس». Transcribed as printed; translated as «ليس».
    {"type": "pair",
     "ar": "يعني: أن الباء ليست صلة لـ«أشبه»؛ إذ لبس الحروف مشابها بها ولا باء السببية، بل ظرف مستقر واقع موقع الحال،",
     "en": "He means: the bāʾ is not the complement (ṣila) of “ashbaha”, since the letters are not [what] it is likened to; nor is it the bāʾ of causation; rather it is a stable adverbial (ẓarf mustaqarr) standing in the position of the circumstantial (ḥāl)."},
    # REVIEW: printed «زيادتهما» (dual) referring to «الحروف», and «مع تفسير بعض الحركات», where «تغيير» would be expected. Transcribed as printed; translated as «تغيير».
    {"type": "pair",
     "ar": "وإنما لم يجعلها للسببية لأصالة الملابسة بالاتفاق، ولأن سببية الحروف للمشابهة بسبب أن زيادتهما في أول الماضي مع تفسير بعض الحركات سبب محصل لجهة مشابهة المضارع الاسم، وهي وقوعه مشتركا، فتكون سببيتها بالواسطة؛",
     "en": "He did not make it [the bāʾ] causal only because accompaniment (mulābasa) is the primary sense by agreement; and because the letters’ being the cause of the resemblance is due to the fact that adding them at the beginning of the past [form], together with changing some of the vowels, is a cause producing the respect in which the muḍāriʿ resembles the noun, namely its occurring as shared; so their causality is by an intermediary;"},
    {"type": "pair",
     "ar": "ولأن سبب المشابهة مبين بقوله: لوقوعه فيحتاج إلى تكلف في اعتبار سببية الحروف.",
     "en": "and because the cause of the resemblance is stated by his words “because of its occurring”, so regarding the letters as causal would require strain."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "على صيغة جمع المؤنث من الإتيان، أو جئن بيان لوجه الملابسة.",
     "en": "On the form of the feminine plural, from al-ityān (coming), [meaning] “they (fem.) came”; an explanation of the manner of the accompaniment."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الظاهر في أوله إلا أنه اختار لفظ المجمع للإشارة إلى امتناع اجتماعها، والظرفية من قبيل ظرفية الجزء للكل، كأنه قيل بأحد حروف هي أوائله.",
     "en": "The evident [wording] would be “at its beginning”, but he chose the plural word to indicate that they cannot come together; and the adverbial relation is of the kind in which the part is contained in the whole, as though it were said: “with one of letters that are its beginnings”."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "إشارة إلى وجه إضافة حروف إلى «نأيت»، وأن الفرق بين المضاف والمضاف إليه بالإفراد والاجتماع.",
     "en": "An indication of the reason for annexing “letters” to “naʾaytu”, and that the difference between the annexed term and the term annexed to is by separateness and togetherness."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أعاد اللام تنصيصا للعطف، وإشارة إلى كون كل من الأمرين وجه المشابهة.",
     "en": "He repeated the lām to make the coordination explicit, and to indicate that each of the two matters is a respect of the resemblance."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أشار بصيغة الجمع إلى أنه يجوز أن يكون مخصص معنى واحد قرائن كثيرة وإلى كثرة الموارد.",
     "en": "By the plural form he indicated that what specifies a single meaning may be many contextual indications, and [he indicated] the multitude of cases."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لم يراع في البيان ترتيب حروف «نأيت» بل راعى قاعدة تصريف الفعل، فإنه يبتدأ من المتكلم الواحد، وينتهي إلى الغائب.",
     "en": "In the exposition he did not observe the order of the letters of “naʾaytu”, but observed the rule of the verb’s conjugation, which begins from the single speaker and ends at the absent [third person]."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "مذكرا كان أو مؤنثا أو مختلطا.",
     "en": "Whether masculine, feminine or mixed."},
]
