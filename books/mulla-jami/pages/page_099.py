# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 99 (printed ٩٨)."""

PAGE_NUMBER = 99
PRINTED_PAGE = "٩٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "سواء كانت هذه الدلالة[[١]]، بحسب الوضع، مثل: «أحمر»، فإنه موضوع لذات ما أخذت مع بعض صفاتها التي هي الحمرة[[٢]].",
     "en": "whether this signification is by [original] coinage, as in “aḥmar” (red), for it is coined for some essence taken together with some of its attributes — namely redness."},
    {"type": "matn",
     "ar": "أو بحسب الاستعمال مثل: «أربع» في «مررت بنسوة أربع»، فإنه موضوع لمرتبة معينة من مراتب العدد، فلا وصفية فيه بحسب الوضع.",
     "en": "or by usage, as in “arbaʿ” (four) in “I passed by four women,” for it is coined for a specific rank among the ranks of number, so there is no adjectival quality in it by [original] coinage."},
    {"type": "matn",
     "ar": "بل قد تعرضه الوصفية كما في المثال المذكور[[٣]]، فإنه لما أجري فيه على «النسوة»، التي هي من قبيل المعدودات لا الأعداد علم أن معناه: «مررت بنسوة موصوفة بالأربعية»[[٤]].",
     "en": "Rather, the adjectival quality may accidentally befall it, as in the example mentioned; for when in it [the word] was made to run [as an attribute] upon “the women,” who are of the category of the counted things, not of the numbers, it is known that its meaning is: “I passed by women qualified by fourness.”"},
    {"type": "matn",
     "ar": "وهذا معنى وصفي عرض له في الاستعمال، لا أصلي بحسب الوضع، والمعتبر في سببية منع الصرف هو الوصف الأصلي لأصالته لا العرضي لعرضيته[[٥]].",
     "en": "This is an adjectival meaning that accidentally befell it in usage, not an intrinsic one by [original] coinage; and what counts in [a thing’s] being a cause of denying full inflection is the intrinsic adjectival quality, on account of its intrinsic character, not the accidental one, on account of its accidental character."},
    {"type": "matn",
     "ar": "فلذلك قال المصنف -رحمه الله تعالى-: (شرطه) أي: شرط",
     "en": "For this reason the author — may Allah the Exalted have mercy on him — said: “(its condition)” — that is, the condition of"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "القرينة على التعميم قوله: «شرطه».",
     "en": "The indication of the generalization is his words: “its condition.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: في «أحمر». والموصول مع الصلة صفة البعض؛ لأنه يأخذ التأنيث من المضاف إليه، مثل: «قطعت بعض أنامله».",
     "en": "That is: in “aḥmar.” The relative pronoun together with its clause is an adjective of “baʿḍ” (some), because it takes its feminine gender from the term annexed to it, as in “I cut off some of his fingertips (qaṭaʿtu baʿḍa anāmilihi).”"},
    {"type": "pair",
     "ar": "قال بعض المحققين: والذكورة أيضا، انتهى.",
     "en": "One of the verifying scholars said: “and masculinity too,” end [of quotation]."},
    {"type": "pair",
     "ar": "وفيه أن مثل الذكورة والأنوثة لو كانت من جملة الصفات التي كان الأخذ معها موجبا للوصفية يلزم أن يكون جميع الأسماء النكرة وصفا؛ لأنها تدل على ذات مبهمة مأخوذة مع الذكورة والأنوثة.",
     "en": "The objection to it is: if the like of masculinity and femininity were among the attributes whose being taken along [with the essence] necessitated adjectival quality, it would follow that all indefinite nouns are adjectives, because they signify an indeterminate essence taken together with masculinity and femininity."},
    {"type": "pair",
     "ar": "فيلزم أن يكون مثل: إنسان وفرس وحيوان وحجارة وتجارة وكتابة وصفا وليس كذلك.",
     "en": "It would then follow that the likes of “human,” “horse,” “animal,” “stones,” “commerce,” and “writing” be adjectives — and that is not so."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يفهم من هذا الكلام أن الوصفية إنما تعرض لأسماء العدد إذا جعلت نعتا لمعدود. وأطلقت عليه دون سائر استعمالاته مع أن كل اسم عدد استعمل مع مميزه يراد منه المعدود، كما صرح الشارح به في مباحث التمييز.",
     "en": "It is understood from this statement that the adjectival quality befalls the number-nouns only when they are made an adjective of a counted thing, and applied to it, to the exclusion of the rest of their usages — even though every number-noun used with its specifier (mumayyiz) has the counted thing intended by it, as the commentator declared explicitly in the discussions of specification (tamyīz)."},
    {"type": "pair",
     "ar": "فلا شك أنه يراد منه حينئذ ذات ما له ذلك المرتبة من مراتب العدد، فيكون أكثر استعمالات العدد، بل جميعها في معنى الوصفية.",
     "en": "So there is no doubt that in that case the essence which possesses that rank among the ranks of number is intended by it, so that most of the usages of number — indeed all of them — are in the sense of adjectival quality."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الصواب: متصفة.",
     "en": "The correct [reading] is: “muttaṣifa” (qualified by)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فإنه في معرض الزوال، فكأنه لم يثبت، والسبب الرافع الأصل، وهو ههنا الصرف لا يكون إلا إذا كان راسخا.",
     "en": "For it is liable to cease, so it is as though it were never established; and the cause that lifts the base [state] — which here is full inflection — does not operate unless it is firmly entrenched."},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: لم يقم لي إلى الآن دليل قاطع على عدم اعتبار الوصف العرضي، والاستدلال بانصراف «أربع» مدخول لجواز أن يكون انصرافه لانتفاء شرط وزن الفعل بقبوله التاء.",
     "en": "Al-Shaykh al-Raḍī said: no conclusive proof has yet been established for me for disregarding the accidental adjectival quality; and the inference [drawn] from the full inflection of “arbaʿ” is defective, since it is possible that its full inflection is due to the absence of the condition of the verbal pattern, [namely] its accepting the tāʾ."},
    {"type": "pair",
     "ar": "وما يقال: من أن التاء في «أربعة» ليست طارية على «أربع» كما هي طارية على «يعمل»؛ لأن أربعة للمذكر وأربعا للمؤنث، والمذكر مقدم في الرتبة على المؤنث ليس بشيء؛ لأنه إذا جاز ألا يعتد بالوزن",
     "en": "As for what is said — that the tāʾ in “arbaʿa” is not an incidental accretion upon “arbaʿ” as it is upon “yaʿmal,” because “arbaʿa” is for the masculine and “arbaʿan” for the feminine, and the masculine is prior in rank to the feminine — it is of no account, because when it is permissible not to reckon with the pattern"},
]
