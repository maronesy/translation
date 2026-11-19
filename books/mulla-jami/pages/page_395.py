# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 395 (printed ٣٩٤)."""

PAGE_NUMBER = 395
PRINTED_PAGE = "٣٩٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «لعدم كونها دالة بالوضع،» at the foot of PDF p. 394.
    {"type": "matn",
     "ar": "وذكرها في باب الأسماء لإجرائها مجراها، وأخذها حكمها، وبنيت لجريها مجرى ما لا تركيب فيه من الأسماء.",
     "en": "…and he mentioned them in the chapter on nouns because they are treated as nouns and take their rule; and they were made indeclinable because they are treated like nouns in which there is no syntactic combination."},
    {"type": "matn",
     "ar": "فالأصوات بهذا الاعتبار: (كل لفظ) إنما قال: «لفظ» ولم يقل: «اسم» لعدم الوضع فيها كما عرفت",
     "en": "So sound words in this respect are (every utterance): he said “utterance” and did not say “noun” only because there is no coinage in them, as you have learned,"},
    {"type": "matn",
     "ar": "(حكي به صوت) أي: أصدر على لسان الإنسان تشبيها بصوت شيء كما عرفت في القسم الثاني من الأصوات الغير المنقولة",
     "en": "(by which a sound is imitated), that is, which is issued on a person’s tongue in likeness to the sound of something, as you learned in the second kind of untransferred sound words,"},
    {"type": "matn",
     "ar": "(أو صوت به للبهائم) يعني: مثلا[[١]]: أي: لإناختها، أو زجرها، أو دعائها، أو غير ذلك.",
     "en": "(or which is sounded to beasts), meaning “for example”, that is, to make them kneel, drive them off, call them, or the like."},
    {"type": "matn",
     "ar": "وإنما قلنا: «مثلا»؛ لأن المتبادر من البهائم ذات القوائم الأربع، فلا يتناول ما هو للطيور، بل لبعض أفراد الإنسان أيضا، كالصبيان والمجانين،",
     "en": "We said “for example” only because what first comes to mind from “beasts” is four-legged creatures, so it would not cover what is for birds, nor indeed what is for some human individuals too, such as children and the insane;"},
    {"type": "matn",
     "ar": "وإذا كان ذكرها على سبيل التمثيل يتناول التعريف كلها.",
     "en": "if their mention is by way of example, the definition covers all of them."},
    {"type": "matn",
     "ar": "(فالأول: كـ«غاق») إذا صوت به إنسان تشبيها بالغراب.",
     "en": "(The first is like “ghāqi”), when a person sounds it in imitation of the crow."},
    {"type": "matn",
     "ar": "(والثاني: كـ«نخ») مشددة أو مخففة عند إناخة البعير،",
     "en": "(The second is like “nakh”), with or without doubling, on making the camel kneel."},
    {"type": "matn",
     "ar": "ولم يذكر المصنف القسم الأول: وهو ما كان صوت الإنسان ابتداء من غير تعلق بالغير.",
     "en": "The Author did not mention the first kind, namely what is a person’s own sound from the outset, without relation to another."},
    {"type": "matn",
     "ar": "قيل: ذلك؛ لأنه لما كان هذان القسمان[[٢]] مع تعلقهما بالغير ملحقين بالأسماء المبنية، كان كون ذلك القسم كذلك أولى، لكونه صوت الإنسان من غير تعلق بغيره.",
     "en": "It has been said: that is because, since these two kinds, despite their relation to another, are attached to the indeclinable nouns, that kind’s being so is all the more fitting, as it is a person’s sound without relation to another."},

    {"type": "section", "ar": "[المركبات]",
     "en": "Compounds (al-Murakkabāt)"},

    {"type": "matn",
     "ar": "(المركبات) أي: المركبات المعدودة من المبنيات (كل اسم) حاصل (من) تركيب",
     "en": "(Compounds), that is, the compounds counted among the indeclinables, are (every noun) resulting (from) the combination…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الأولى ألا يجعل ذكر البهائم للتمثيل حتى يشمل الطيور وغيرها، بل يجعل التعليل للتمثيل ليشمل دواعي أخرى للتصويت به من قضاء تعجب أو تسكين توجع أو تخفيف تحسر،",
     "en": "It is better not to make the mention of beasts an example so that it covers birds and others, but to make the reason [given] an example, so that it covers other motives for sounding it, such as giving vent to wonder, calming pain, or easing regret;"},
    {"type": "pair",
     "ar": "فيشمل القسم الأول أيضا بتكلف واحد لا بد منه لغير دخول هذا القسم.",
     "en": "then it covers the first kind as well, with a single strain that is unavoidable in any case, apart from the inclusion of this kind."},
    {"type": "pair",
     "ar": "وأما ما وجهه به الشارح اقتفاء للفاضل الهندي، فهو على ما ترى فدع ما كدر وخذ ما صفا.",
     "en": "As for the explanation the Commentator gave, following al-Fāḍil al-Hindī, it is as you see; so leave what is turbid and take what is clear."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قائله: الفاضل الهندي رحمه الله تعالى كأنه أراد أن المتعلق بالغير كما في تصويت البهائم، فإن الصوت يلقى إلى البهيمة، وكما في حكاية الصوت، فإنه لإسماع الغير",
     "en": "Its proponent is al-Fāḍil al-Hindī, may Allah the Exalted have mercy on him. He seems to have meant that what is related to another, as in sounding to beasts, for the sound is cast to the beast, and as in imitating a sound, for it is to make another hear,"},
    {"type": "pair",
     "ar": "ذلك الصوت أقرب من المركب مع الغير؛ لأنه لتفهيم الغير لا محالة،",
     "en": "that sound is nearer to what is combined with another, because it is necessarily for making another understand;"},
    {"type": "pair",
     "ar": "وما لم يتعلق بالغير كوى للمتعجب، فإنه يتلفظ به بمقتضى الطبع من غير نظر إلى الغير في غاية البعد من التركيب مع الغير،",
     "en": "whereas what is not related to another, like “way” from one who wonders, which is uttered by natural impulse without regard to another, is extremely remote from combination with another."},
    {"type": "pair",
     "ar": "فإذا لم يكن ما هو أقرب إلى الغير معربا، فما هو أبعد منه بطريق الأولى ألا يكون معربا،",
     "en": "So if what is nearer to another is not declinable, then what is further from it is all the more not declinable."},
    {"type": "pair",
     "ar": "وفيه أن بعده عن الإعراب لا يوجب أولوية إلحاقها بالمبني لجواز سقوطها عن درجة الاعتبار بحيث لا يكون ملحقة بالأسماء المبنية أيضا.",
     "en": "Against this: its remoteness from declension does not entail that attaching it to the indeclinable is more fitting, since it may fall below the level of consideration altogether, so as not to be attached to the indeclinable nouns either."},
]
