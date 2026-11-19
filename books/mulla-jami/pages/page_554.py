# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 554 (printed ٥٥٣)."""

PAGE_NUMBER = 554
PRINTED_PAGE = "٥٥٣"   # Arabic-Indic, as printed

BLOCKS = [
    {"type": "section", "ar": "[الحروف المشبهة بالفعل]",
     "en": "The Particles Resembling the Verb (al-Ḥurūf al-Mushabbaha bi-l-Fiʿl)"},

    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(الحروف المشبهة بالفعل[[١]]) وجه شبهها به:",
     "en": "(The particles resembling the verb): the respect in which they resemble it is"},
    {"type": "matn",
     "ar": "أما لفظا: فلانقسامها كالفعل إلى الثلاثي الرباعي والخماسي، ولبنائها على الفتح مثله.",
     "en": "in wording, because, like the verb, they divide into triliteral, quadriliteral and quinqueliteral, and because they are fixed on the fatḥa, as it is;"},
    {"type": "matn",
     "ar": "وأما معنى: فلأن معانيها معاني الأفعال[[٢]]، مثل: «أكدت[[٣]]، وشبهت، واستدركت، وتمنيت، وترجيت».",
     "en": "and in meaning, because their meanings are the meanings of verbs, such as “I have corroborated, I have likened, I have rectified, I have wished, I have hoped”."},
    {"type": "matn",
     "ar": "وكان المناسب أن يعبر عنها بالأحرف المشبهة، على صيغة جمع القلة؛ لكونها ستة،",
     "en": "It would have been fitting to refer to them as “al-aḥruf al-mushabbaha”, in the form of the plural of paucity (jamʿ al-qilla), since they are six;"},
    {"type": "matn",
     "ar": "لكنهم لما عبروا عن الحروف الجارة والعاطفة مثلا بصيغة جمع الكثرة لم يستحسنوا تغيير الأسلوب",
     "en": "but since they had referred to the prepositions and the coordinating particles, for example, with the form of the plural of multitude (jamʿ al-kathra), they did not consider it good to change the manner of expression,"},
    {"type": "matn",
     "ar": "مع شيوع استعمال كل من صيغتي جمع القلة والكثرة مع الأخرى،",
     "en": "given the common use of each of the two forms, the plural of paucity and of multitude, in place of the other;"},
    {"type": "matn",
     "ar": "على أنها إذا لوحظت مع فروعها الحاصلة بتخفيف نوناتها، ولغات «لعل» تبلغ مبلغ جمع الكثرة.",
     "en": "moreover, when they are considered together with their derived forms arising from lightening their nūns, and the dialectal variants of “laʿalla”, they reach the number of the plural of multitude."},
    {"type": "matn",
     "ar": "(وهي: «إن، وأن، وكأن، ولكن، وليت، ولعل») أخرهما[[٤]] لكونهما للإنشاء، بخلاف الأربعة السابقة.",
     "en": "(They are: inna, anna, kaʾanna, lākinna, layta and laʿalla). He put the last two last because they are for the performative (inshāʾ), unlike the four preceding ones."},
    {"type": "matn",
     "ar": "(لها) أي: لهذه الحروف (صدر الكلام) وجوبا، ليعلم من أول الأمر[[٥]] أنه أي قسم من أقسام الكلام؛",
     "en": "(They have), that is, these particles have, (the head of the sentence) necessarily, so that it may be known from the outset which of the kinds of speech it is;"},
    {"type": "matn",
     "ar": "إذ كل منها يدل على قسم منه، كالكلام المؤكد والمشتمل على التشبيه والاستدراك والتمني والترجي.",
     "en": "for each of them indicates one kind of it, such as corroborated speech, and speech containing likening, rectification (istidrāk), wishing and hoping."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: اعتبر شبهها بالفعل للإعمال، ولذا قال: وجه شبهها أي: وجه المشابهة التي اعتبرت، ولم يقل: يعتبر وجه شبهها.",
     "en": "That is, their resemblance to the verb is taken into account for [their] governing; hence he said “the respect in which they resemble it”, that is, the respect of the resemblance that has been taken into account, and did not say “the respect of their resemblance is taken into account”."},
    {"type": "pair",
     "ar": "قال العصام: كان الأنسب تقديمها على الحروف الجارة على طبق تقديم المرفوع والمنصوب على المجرور",
     "en": "Al-ʿIṣām said: it would have been more fitting to place them before the prepositions, in accordance with placing the nominative and the accusative before the genitive,"},
    {"type": "pair",
     "ar": "إلا أنه راعى أصالة حروف الجر في عملها، وفرعية هذه الحروف.",
     "en": "except that he observed that the prepositions are original in their governing, and that these particles are derivative."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: «لكون كل منهما» printed with a dual pronoun although the referent is plural; transcribed as printed.
    {"type": "pair",
     "ar": "لكون كل منهما معاني جزئية لا باعتبار النسبة إلى الفاعل المعين في مفهوم الأفعال كالحروف.",
     "en": "Because each of the two [sets of] meanings is particular, not in respect of the relation to the determinate agent in the concept of verbs, like [the meanings of] particles."},
    {"type": "pair",
     "ar": "قال العصام: لم يرد أن هذه الأحرف بمعنى الأفعال الماضية؛ لأن الظاهر أنها إنشاء التأكيد، والتشبيه، والترجي، والتمني في الحال،",
     "en": "Al-ʿIṣām said: he did not mean that these particles are in the sense of past verbs, because what is apparent is that they are the performative enactment of corroboration, likening, hoping and wishing in the present;"},
    {"type": "pair",
     "ar": "فالتعبير عن معانيها بالأفعال الماضية؛ لأنها بمعنى الأفعال المقصودة بها الإنشاء، والشائع استعمال الماضي في الإنشاء كصيغ العقود.",
     "en": "so expressing their meanings by past verbs is because they are in the sense of verbs by which the performative is intended, and the common usage is to employ the past tense for the performative, as in the formulae of contracts."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "بصيغة الماضي المستعملة للإنشاء الدالة على تحقق معانيها لكون الحروف كذلك.",
     "en": "In the past-tense form used for the performative, which indicates the realization of their meanings, since the particles are likewise."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "مع أن كونها ثلاثية ورباعية وخماسية، يقتضي خلاف هذا الترتيب.",
     "en": "Even though their being triliteral, quadriliteral and quinqueliteral requires an order other than this."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: يعلم السامع من أول الأمر، وهذا العلم واجب دفعا لحيرة السامع وتوهمه أولا معنى غير ما أفاده المتكلم.",
     "en": "That is, the hearer knows from the outset; and this knowledge is necessary to forestall the hearer’s perplexity and his imagining at first a meaning other than what the speaker conveyed."},
]
