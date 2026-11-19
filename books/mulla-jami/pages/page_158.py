# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 158 (printed ١٥٧)."""

PAGE_NUMBER = 158
PRINTED_PAGE = "١٥٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(مثل) قوله تعالى: (﴿ولعبد مؤمن خير من مشرك﴾[[١]])،",
     "en": "…(as in) His words, the Exalted: (“And a believing slave is better than an idolater”—wa-la-ʿabdun muʾminun khayrun min mushrikin),"},
    {"type": "matn",
     "ar": "فإن «العبد» متناول للمؤمن والكافر، وحيث وصف بالمؤمن تخصص بالصفة[[٢]]، فجعل مبتدأ، و«خير» خبره.",
     "en": "for “slave” (ʿabd) covers the believer and the unbeliever; and since it was qualified by “believing” it was specified by the adjective, so it was made a mubtadaʾ, and “khayr” (better) its khabar."},
    {"type": "matn",
     "ar": "(و) مثل قولك: («أرجل في الدار أم امرأة»[[٣]]) فإن المتكلم بهذا الكلام يعلم[[٤]] أن أحدهما في الدار، فيسأل المخاطب عن تعيينه،",
     "en": "(And) as in your saying: (“Is a man in the house, or a woman?”—a-rajulun fī al-dāri ami mraʾatun); for the one who speaks these words knows that one of the two is in the house, and so asks the addressee to identify it;"},
    {"type": "matn",
     "ar": "فكأنه قال: أي الأمرين المعلوم كون أحدهما في الدار كائن فيها؟",
     "en": "so it is as if he said: which of the two things, one of which is known to be in the house, is in it?"},
    {"type": "matn",
     "ar": "فكل واحد منهما تخصص بهذه الصفة، فجعل «الرجل» مبتدأ، و«في الدار» خبره.",
     "en": "Thus each of the two has been specified by this attribute, so “the man” (al-rajul) was made a mubtadaʾ, and “in the house” (fī al-dār) its khabar."},
    {"type": "matn",
     "ar": "(و) مثل قولك: («ما أحد خير منك») فإن النكرة فيها وقعت في حيز النفي، فأفادت عموم الأفراد وشمولها، فتعينت وتخصصت[[٥]]،",
     "en": "(And) as in your saying: (“No one is better than you”—mā aḥadun khayrun minka); for the indefinite noun in it occurs within the scope of negation, and so conveys the generality of the individuals and their comprehensiveness, and thereby becomes determinate and specified;"},
    {"type": "matn",
     "ar": "فإنه لا تعدد في جميع الأفراد[[٦]]، بل هو أمر واحد،",
     "en": "for there is no multiplicity in “all the individuals”; rather, it is a single thing."},
    {"type": "matn",
     "ar": "وكذا كل نكرة في الإثبات قصد بها العموم، نحو: «تمرة خير من جرادة»[[٧]].",
     "en": "Likewise every indefinite noun in an affirmative [statement] by which generality is intended, as in: “A date is better than a locust” (tamratun khayrun min jarādatin)."},
    {"type": "matn",
     "ar": "(و) مثل قولهم: (شر أهر ذا ناب) لتخصصه بما يتخصص به الفاعل[[٨]] لشبهه به؛",
     "en": "(And) as in their saying: (“An evil made the fanged one snarl”—sharrun aharra dhā nābin), because it is specified by that by which the agent is specified, on account of its resemblance to it;"},
    {"type": "matn",
     "ar": "إذ يستعمل في موضع «ما أهر ذا ناب إلا شر»[[٩]]، وما يتخصص به الفاعل قبل ذكره",
     "en": "for it is used in place of “Nothing but an evil made the fanged one snarl” (mā aharra dhā nābin illā sharrun); and that by which the agent is specified before it is mentioned…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة البقرة، ٢٢١.",
     "en": "Qurʾān, Sūrat al-Baqara 2:221."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قيل: لا معنى لعدم صحة «إنسان خير من فرس»، وصحة «حيوان ناطق خير من فرس»، بل صحة «جسم نام خير من حجر»؟",
     "en": "It is said: what sense is there in “A human is better than a horse” (insānun khayrun min farasin) being invalid, while “A rational animal is better than a horse” is valid—indeed, while “A growing body is better than a stone” is valid?"},
    {"type": "pair",
     "ar": "قلت: ما ذكر سر نحوي لالتزام العرب تخصيص النكرة في مقام الابتداء، ولا مناقشة في الأسرار لذوي الأبصار.",
     "en": "I say: what has been mentioned is a grammatical rationale (sirr) for the Arabs’ adherence to specifying the indefinite noun in the position of the mubtadaʾ; and there is no disputing over rationales for those of insight."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ومما يتخصص بوجه ما جواب هذا الاستفهام، فإنه يصح أن يقال: رجل أو يقال: امرأة،",
     "en": "Among what is specified in some way is the answer to this question; for it is valid to say: “A man,” or to say: “A woman,”"},
    {"type": "pair",
     "ar": "فإنه تخصص بعلم المخاطب بثبوته في الدار على وجه الاحتمال، فكأنه قال: رجل احتمله عندك أنه في الدار.",
     "en": "for it has been specified by the addressee’s knowledge of its presence in the house by way of possibility; so it is as if he said: “A man of whom it was possible, in your view, that he is in the house.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فيه أن هذا التخصيص عند المتكلم؛ لأنه يعلم كون أحدهما في الدار، والاختصاص المصحح هو الاختصاص عند المخاطب.",
     "en": "There is [an objection] here: this specification is [only] in the view of the speaker, since it is he who knows that one of the two is in the house, whereas the specificity that validates [the mubtadaʾ] is specificity in the view of the addressee."},
    {"type": "pair",
     "ar": "وفيه أيضا: أن هذا التخصيص منتف في مثل «أرجل في الدار؟». فينبغي أن يمتنع الابتداء به مع أنه صحيح.",
     "en": "There is also [the objection] that this specification is absent in such as “Is a man in the house?” (a-rajulun fī al-dār?); so beginning with it ought to be excluded, although it is valid."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يعني: أن المراد بالتخصيص ههنا: التعيين بقطع الاحتمالات أو تقليلها،",
     "en": "He means: what is meant by specification here is determination by cutting off the possibilities or reducing them;"},
    {"type": "pair",
     "ar": "فلا يرد ما قيل من ألا تخصيص ههنا؛ لأن التخصيص أن يجعل لبعض من الجملة شيء ليس لسائر أمثاله.",
     "en": "so there is no force in what has been said, that there is no specification here because specification is that something be assigned to some part of the whole that does not belong to the rest of its like."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "خلاصة هذا الوجه جار فيما إذا أريد بالنكرة نفس الطبيعة، فإنه لا تعدد فيها بل هي أمر واحد.",
     "en": "The gist of this explanation applies [also] when the nature (ṭabīʿa) itself is intended by the indefinite noun; for there is no multiplicity in it, but it is a single thing."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "هذا قول أمير المؤمنين عمر رضي الله عنه في تعيين فدية الجرادة إذا قتله من أحرم،",
     "en": "This is the saying of the Commander of the Faithful ʿUmar, may Allah be pleased with him, in determining the expiation (fidya) for a locust when one in the state of iḥrām kills it;"},
    {"type": "pair",
     "ar": "والمقصود أنه يتصدق بما شاء.",
     "en": "and what is meant is that he gives in charity whatever he wishes."},
    {"type": "pair",
     "ar": "وعموم النكرة مع الإثبات في المبتدأ كثير، وفي الفاعل قليل نحو: ﴿علمت نفس ما قدمت وأخرت﴾ (سورة الانفطار:٥)،",
     "en": "The generality of the indefinite noun in the affirmative is frequent in the mubtadaʾ and rare in the agent, as in: “A soul will know what it has sent forth and left behind” (Qurʾān, Sūrat al-Infiṭār 82:5);"},
    {"type": "pair",
     "ar": "بخلاف ما في حيز النفي، فإنه يستوي فيه المبتدأ والفاعل وغيرهما.",
     "en": "unlike what is within the scope of negation, for in it the mubtadaʾ, the agent and others are alike."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "لا يخفى ما فيه من التكلف؛ لأنه جعل بمنزلة ما في تخصيصه خفاء.",
     "en": "The strain in this is not hidden; for it has been placed on the level of that whose specification is obscure."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "أو لأنه كان في الأصل فاعلا لـ«أهر» قدم لإفادة التخصيص والحصر.",
     "en": "Or because it was originally the agent of “aharra,” and was placed first to convey specification and restriction (ḥaṣr)."},
]
