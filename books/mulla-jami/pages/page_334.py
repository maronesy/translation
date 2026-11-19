# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 334 (printed ٣٣٣)."""

PAGE_NUMBER = 334
PRINTED_PAGE = "٣٣٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «لأنه يدل على» at the foot of PDF p. 333.
    {"type": "matn",
     "ar": "الذات، لا على قيام معنى بها،",
     "en": "…the essence, not that a meaning subsists in it."},
    {"type": "matn",
     "ar": "فكأنه لم يقع في بعض النسخ قوله: «ولا يوصف به» ولهذا اعتذر الشارح الرضي وقال: لم يذكر المصنف أنه لا يوصف بالضمير؛ لأنه تبين ذلك بقوله:",
     "en": "It seems that his words “nor is [anything] qualified by it” did not occur in some copies; that is why the commentator al-Raḍī offered an excuse, saying: The author did not mention that nothing is qualified by the pronoun, because that is made clear by his words:"},
    {"type": "matn",
     "ar": "(والموصوف أخص أو مساو) أي: الموصوف المعرفة أشد اختصاصا[[١]] بالتعريف والمعلومية من الصفة، يعني: أعرف منها؛",
     "en": "(The qualified is more specific or equal), that is, the definite qualified noun is more particularly marked by definiteness and being known than the adjective, meaning more definite than it;"},
    {"type": "matn",
     "ar": "لأنه المقصود[[٢]] الأصلي، فيجب أن يكون أكمل من الصفة في التعريف أو مساويا لها؛",
     "en": "for it is the principal object of intent, so it must be more complete than the adjective in definiteness, or equal to it;"},
    {"type": "matn",
     "ar": "لأنه لو لم يكن أكمل منها فلا أقل من ألا يكون أدون منها،",
     "en": "for if it is not more complete than it, then at the least it must not be lower than it."},
    {"type": "matn",
     "ar": "والمنقول عن سيبويه، وعليه جمهور النحاة: أن أعرفها المضمرات[[٣]]، ثم الأعلام، ثم اسم الإشارة، ثم المعرف باللام والموصولات[[٤]]، فبينهما مساواة.",
     "en": "What is transmitted from Sībawayh, and held by the majority of grammarians, is that the most definite of them are the pronouns, then proper names, then the demonstrative noun, then the noun made definite by the lām and the relative nouns, between which two there is equality."},
    {"type": "matn",
     "ar": "(ومن ثمة) أي: ومن أجل أن الموصوف أخص أو مساو (لم يوصف ذو اللام إلا بمثله) أي: ذي اللام الآخر أو الموصول،",
     "en": "(Hence), that is, because the qualified is more specific or equal, (a noun with the lām is qualified only by its like), that is, by another noun with the lām, or by a relative noun,"},
    {"type": "matn",
     "ar": "فإنه أيضا مماثل لذي اللام، لما عرفت أن بينهما من المساواة في التعريف",
     "en": "for that too is the like of the noun with the lām, since you have learned that there is equality in definiteness between them,"},
    {"type": "matn",
     "ar": "نحو: «جاءني الرجل الفاضل، أو الرجل الذي كان عندك أمس»",
     "en": "as in “The excellent man came to me” or “The man who was with you yesterday [came to me]”;"},
    {"type": "matn",
     "ar": "(أو بالمضاف إلى مثله) أي: مثل المعرف باللام بلا واسطة نحو: «جاءني الرجل صاحب الفرس»، أو بواسطة نحو: «جاءني الرجل صاحب لجام الفرس»؛ لأن",
     "en": "(or by what is annexed to its like), that is, to the like of the noun made definite by the lām, either without intermediary, as in “The man, owner of the horse, came to me,” or with an intermediary, as in “The man, owner of the horse’s bridle, came to me”; because…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ومنهم من حمل الأخص والمساوي على ما هو مصطلح المنطقيين عليه، وهو الأخص والمساوي بحسب الصدق، وذلك باطل.",
     "en": "Some took “more specific” and “equal” in the sense of the logicians’ technical usage, namely more specific and equal with respect to extension (bi-ḥasab al-ṣidq); and that is false."},
    {"type": "pair",
     "ar": "أما أولا: فلأن الموصوف معرفة كان أو نكرة قد يكون أعم نحو: الحيوان الناطق أو حيوان ناطق، والحمل على الخصوص والمساواة بعد التوصيف مما لا فائدة فيه.",
     "en": "First, because the qualified, whether definite or indefinite, is sometimes more general, as in “the rational animal” or “a rational animal”; and taking [specificity and equality] to hold after the qualification is of no benefit."},
    {"type": "pair",
     "ar": "وأما ثانيا فلأنه لا يصح بناء.",
     "en": "Second, because [the conclusion drawn from it] cannot soundly be built on it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ولا يجوز أن يكون المقصود الأصلي منحطا في الرتبة عما ليس مقصودا.",
     "en": "It is not permissible for the principal object of intent to be lower in rank than what is not intended."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: كون المتكلم والمخاطب أعرف ظاهر. وأما الغائب فلأن احتياجه إلى لفظ يفسره جعله بمنزلة وضع اليد.",
     "en": "Shaykh al-Raḍī said: That the speaker and the addressee are the most definite is evident. As for the absent [third person], its need for a word that explains it has put it on a par with laying the hand [on the thing]."},
    {"type": "pair",
     "ar": "وإنما كان العلم أعرف من اسم الإشارة؛ لأن مدلول العلم ذات معينة مخصوصة عند الوضع والاستعمال بخلاف اسم الإشارة،",
     "en": "The proper name is more definite than the demonstrative noun only because what the proper name signifies is a specified, particular essence both at coinage and in use, unlike the demonstrative noun;"},
    {"type": "pair",
     "ar": "فإن مدلوله عند الوضع غير معين، وإنما تعيينه بالإشارة الحسية، وكثيرا ما يقع اللبس في المشار إليه إشارة حسية،",
     "en": "for what it signifies at coinage is unspecified, and it is specified only by sensory pointing, and confusion often arises regarding what is pointed to by sensory pointing."},
    {"type": "pair",
     "ar": "فلذلك كان أكثر أسماء الإشارة موصوفا في كلامهم. ولهذا لم يفصل بين اسم الإشارة ووصفه لشدة احتياجه إليه.",
     "en": "For that reason most demonstrative nouns are qualified in their speech; and for this reason no separation is made between the demonstrative noun and its qualifier, because of its great need of it."},
    {"type": "pair",
     "ar": "وإنما كان اسم الإشارة أعرف من المعرف باللام؛ لأن المخاطب يعرف مدلول اسم الإشارة بالقلب والعين معا، ومدلول المعرف باللام يعرف بالقلب دون العين والموصول كذا اللام.",
     "en": "The demonstrative noun is more definite than the noun made definite by the lām only because the addressee knows what the demonstrative signifies by heart and eye together, whereas what the noun with the lām signifies is known by the heart and not the eye; and the relative noun is like the lām."},
    {"type": "pair",
     "ar": "وأما المضاف إلى أحد الأربعة، فتعريفه مثل تعريف المضاف إليه سواء؛ لأنه يكتسب التعريف منه هذا عند سيبويه.",
     "en": "As for what is annexed to one of the four, its definiteness is exactly that of the noun to which it is annexed, because it acquires definiteness from it. This is according to Sībawayh."},
    {"type": "pair",
     "ar": "وأما عند المبرد فتعريفه أنقص. ولذا يوصف المضاف إلى المضمر ولا يوصف المضمر.",
     "en": "According to al-Mubarrad, its definiteness is less; that is why what is annexed to a pronoun is qualified while the pronoun is not."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "بقي المضاف إلى المعرفة، ولم يتعرض له؛ لأنه يجيء بعد، والمنادى،",
     "en": "There remain what is annexed to a definite noun—he did not address it because it comes later—and the vocative (munādā);"},
    {"type": "pair",
     "ar": "والقياس أن يكون في مرتبة ضمير المخاطب، ولكن وصفه دون ضمير المخاطب يدل على أنه أنقص منه.",
     "en": "analogy requires that it be of the rank of the second-person pronoun, but its being qualified, unlike the second-person pronoun, shows that it is lower than it."},
]
