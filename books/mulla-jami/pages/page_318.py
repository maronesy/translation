# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 318 (printed ٣١٧)."""

PAGE_NUMBER = 318
PRINTED_PAGE = "٣١٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # New sentence: the matn on PDF p. 317 ends «وعلى هذا القياس «أخلاق ثياب».»
    {"type": "matn",
     "ar": "(ولا يضاف اسم مماثل) أي: مشابه (للمضاف إليه في العموم والخصوص[[١]]) إلى ذلك المضاف إليه",
     "en": "(A noun that is equivalent), that is, similar, (to the term annexed to in generality and particularity is not annexed) to that term,"},
    {"type": "matn",
     "ar": "سواء كانا مترادفين[[٢]] (كـ«ليث وأسد») في الأعيان والجثث[[٣]] (وحبس ومنع) في المعاني والأحداث، أو غير مترادفين بل متساويين في الصدق كالإنسان والناطق",
     "en": "whether the two are synonyms—(like “layth” and “asad,” both meaning lion) among concrete things and bodies, (and “ḥabs” and “manʿ,” both meaning restraint) among meanings and events—or not synonyms but coextensive in application, like “human” and “rational,”"},
    {"type": "matn",
     "ar": "(لعدم الفائدة) في ذكر المضاف إليه، فإنك إذا قلت: «رأيت ليث أسد» لا يفيد إلا ما يفيده «رأيت ليثا» بدون ذكر الأسد، وإضافة الليث إليه،",
     "en": "(because there is no benefit) in mentioning the term annexed to; for if you say “raʾaytu laytha asadin,” it conveys only what “raʾaytu laythan” (I saw a lion) conveys without mentioning “asad” and annexing “layth” to it;"},
    {"type": "matn",
     "ar": "فيكون ذكر الأسد وإضافة الليث إليه لغوا[[٤]] لا فائدة فيه",
     "en": "so mentioning “asad” and annexing “layth” to it is redundant, without benefit,"},
    {"type": "matn",
     "ar": "(بخلاف) إضافة العام إلى الخاص[[٥]] في مثل: («كل الدراهم، وعين الشيء»[[٦]]، فإنه) أي: المضاف[[٧]] فيهما (يختص[[٨]] به) أي: يصير خاصا بسبب إضافته إلى المضاف إليه، ولا يبقى على عمومه",
     "en": "(unlike) the annexation of the general to the particular in such as (“kullu l-darāhimi” [all the dirhams] and “ʿaynu l-shayʾi” [the thing itself], for it), that is, the annexed term in both, (is particularized by it), that is, it becomes particular by being annexed to the term annexed to, and does not remain in its generality,"},
    {"type": "matn",
     "ar": "سواء أفادت[[٩]] الإضافة التعريف أو التخصيص،",
     "en": "whether the annexation conveys definiteness or specification."},
    {"type": "matn",
     "ar": "وأعمية العين عن الشيء إذا كان اللام فيه للعهد ظاهرة. وأما إذا كان للجنس ففيهما خفاء[[١٠]].",
     "en": "That “ʿayn” is more general than “al-shayʾ” is evident when the article in the latter is for definite reference (ʿahd); but when it is generic, there is obscurity in both."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أراد بالمماثلة في العموم أن يكون مدلولاهما كليين، ويتحد أفرادهما سواء كانا مترادفين أو متساويين،",
     "en": "By equivalence in generality he means that what the two denote are universals whose individuals coincide, whether they are synonyms or coextensive;"},
    {"type": "pair",
     "ar": "وبالمماثلة في الخصوص أن يكون مدلولهما شخصا واحدا،",
     "en": "and by equivalence in particularity, that what they denote is one individual."},
    {"type": "pair",
     "ar": "والأخصر الأوضح، ولا يضاف أحد المترادفين أو المتساويين إلى الآخر،",
     "en": "The more concise and clearer [wording would be]: “one of two synonyms or of two coextensive terms is not annexed to the other.”"},
    {"type": "pair",
     "ar": "وينبغي ألا يقتصر عليه، بل يضم إليه أنه لا يضاف الأخص من حيث إنه الأخص إلى الأعم،",
     "en": "He ought not to have confined himself to this, but should have added that the more particular, qua more particular, is not annexed to the more general."},
    {"type": "pair",
     "ar": "وكأنه اقتصر على ما ذكره لأنه وقع في اللغة ما يوهم وقوعه من كل الدراهم، وعين الشيء، وسعيد كرز، فأراد دفعه.",
     "en": "It seems he confined himself to what he mentioned because there occur in the language cases that suggest it occurs—“kullu l-darāhimi,” “ʿaynu l-shayʾi,” and “Saʿīdu Kurzin”—and he wished to dispel that."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أجاز الفراء إضافة أحد المترادفين إلى الآخر للتخفيف متمسكا بالاستعمال، وتبعه الشيخ الرضي.",
     "en": "Al-Farrāʾ permitted annexing one of two synonyms to the other for lightening, relying on usage, and Shaykh al-Raḍī followed him."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "في الصحاح والقاموس: الجثة: شخص الإنسان، فهو أخص من الأعيان.",
     "en": "In al-Ṣiḥāḥ and al-Qāmūs: al-juththa is a person’s bodily form; so it is more particular than “concrete things” (aʿyān)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لأنه ليس في ذكر المضاف إليه فائدة بخلاف المضاف إليه بالإضافة اللفظية،",
     "en": "Because there is no benefit in mentioning the term annexed to, unlike the term annexed to in formal annexation;"},
    {"type": "pair",
     "ar": "ولا في الإضافة لأنه لا تخفيف بها؛ إذ حذف المضاف إليه أخف.",
     "en": "nor in the annexation, because no lightening comes of it, since dropping the term annexed to is lighter."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "جعل قوله: بخلاف متعلقا بقوله: لعدم الفائدة.",
     "en": "He made his words “unlike” connected with his words “because there is no benefit.”"},
    {"type": "pair",
     "ar": "ويحتمل أن يتعلق بالأمثلة أي: الاسم المماثل كليث وأسد بخلاف كل الدراهم وعين الشيء،",
     "en": "It may also be connected with the examples, that is: the equivalent noun, like “layth” and “asad,” as opposed to “kullu l-darāhimi” and “ʿaynu l-shayʾi”;"},
    {"type": "pair",
     "ar": "فإن الكل ليس فيه مماثل الدراهم والعين ليس مماثل الشيء، بل يختص بالإضافة.",
     "en": "for in “kull” there is nothing equivalent to “the dirhams,” and “ʿayn” is not equivalent to “al-shayʾ”; rather it is particularized by the annexation."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وكذا حي زيد أي: ذاته وشخصه، واسم السلام عليكما، أي: كلمة السلام ولفظه، والمشهور أن اسما مقحم.",
     "en": "Likewise “ḥayyu Zaydin,” that is, his very self and person, and “ismu l-salāmi ʿalaykumā” (the name of peace be upon you both), that is, the word and expression of “peace”; the well-known view is that “ism” is intrusive (muqḥam)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لم يجعل الضمير راجعا إلى المضاف إليه؛ لأن قوله يختص ينبئ عن حدوث الاختصاص، وهو في المضاف دون المضاف إليه، ولأن الكلام مسوق لفائدة الإضافة.",
     "en": "He did not take the pronoun as referring to the term annexed to, because his word “is particularized” indicates that particularization comes about, and this is in the annexed term, not the term annexed to; and because the discussion is framed around the benefit of annexation."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "بالاختصاص التعريفي أو غيره، وإليه أشار بقوله: سواء إلى آخره.",
     "en": "By particularization through definiteness or otherwise; he points to this with his words “whether …” to the end."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "يعني: أن الاختصاص ليس بمعنى التخصيص المقابل للتعريف، فيصح المثالان.",
     "en": "That is, particularization here does not mean the specification that is contrasted with definiteness; so both examples hold."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "اعلم أن الشيء بمعنى الموجود في الخارج عند جماعة، ولا شبهة في أن العين بمعنى الذات أعم منه،",
     "en": "Know that “al-shayʾ” (thing) means, according to one group, what exists extramentally, and there is no doubt that “ʿayn” in the sense of essence (dhāt) is more general than it;"},
    {"type": "pair",
     "ar": "وبمعنى مساو للموجود المطلق الشامل للموجود الذهني والخارجي عند جماعة.",
     "en": "and according to another group it means what is coextensive with existent without qualification, which includes the mental and the extramental existent."},
    {"type": "pair",
     "ar": "وعلى هذا لم يكن العين أعم منه لشموله على كل مفهوم.",
     "en": "On this view “ʿayn” would not be more general than it, since it covers every concept."},
    {"type": "pair",
     "ar": "هذا إذا أريد بالشيء نفس مفهومه مع قطع النظر عن تحققه في",
     "en": "This is if by “al-shayʾ” its concept itself is meant, disregarding its realization in…"},
]
