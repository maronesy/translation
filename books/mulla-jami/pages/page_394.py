# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 394 (printed ٣٩٣)."""

PAGE_NUMBER = 394
PRINTED_PAGE = "٣٩٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows the division of sounds stated at the foot of PDF p. 393 (new sentence).
    {"type": "matn",
     "ar": "فالأول: مثل: «واها» للتعجب، وحكمه حكم المصادر.",
     "en": "The first is like “wāhan”, for wonder; its rule is the rule of maṣdars."},
    {"type": "matn",
     "ar": "والثاني: مثل: «مه وصه»، وحكمه حكم أسماء الأفعال.",
     "en": "The second is like “mah” and “ṣah”; its rule is the rule of verbal nouns."},
    {"type": "matn",
     "ar": "وإما غير منقولة، بل باقية على ما كانت عليه حين كونها أصواتا ساذجة، ولم تصر مصادر ولا أسماء أفعال، وهي على أنواع:",
     "en": "Or they are not transferred, but remain as they were when they were bare sounds, and have become neither maṣdars nor verbal nouns. These are of several kinds."},
    {"type": "matn",
     "ar": "فمنها: ما يعرض للإنسان عند عروض معنى له، كقول المتندم أو المتعجب «وي، وخ»، لا يقدر أن يحكم عليه بشيء، أو به على شيء.",
     "en": "Among them is what occurs to a person when some state comes upon him, as when one who regrets or wonders says “way” or “wakh”; nothing can be predicated of it, nor can it be predicated of anything."},
    {"type": "matn",
     "ar": "ومنها: ما يجري على لفظ الإنسان على سبيل الحكاية، بأن يصدر من نفسه ما يشابه صوت شيء،",
     "en": "Among them is what runs on a person’s tongue by way of imitation (ḥikāya), in that he produces from himself something resembling the sound of a thing,"},
    {"type": "matn",
     "ar": "كما إذا قلت: «غاق» قاصدا لإصدار ما يشابه صوت الغراب عن نفسك، وحينئذ لا تقدر أن يحكم عليه أو به.",
     "en": "as when you say “ghāqi”, intending to produce from yourself something resembling the crow’s call; in that case you cannot have anything predicated of it or have it predicated of anything."},
    {"type": "matn",
     "ar": "ومنها: ما يصوت به لأجل حيوان: إما لزجر، أو دعاء، أو غير ذلك[[١]]، كما إذا قلت: «نخ» لإناخة البعير، وحينئذ أيضا لا يقدر أن يحكم عليه أو به.",
     "en": "Among them is what is sounded for an animal, whether to drive it off, to call it, or for something else, as when you say “nakh” to make a camel kneel; here too nothing can be predicated of it, nor can it be predicated of anything."},
    {"type": "matn",
     "ar": "وهذه الأقسام كلها مبنيات؛ لانتفاء التركيب فيها[[٢]]،",
     "en": "All these kinds are indeclinable, because there is no syntactic combination (tarkīb) in them."},
    {"type": "matn",
     "ar": "وإذا تلفظ بها على سبيل الحكاية، كما إذا قلت: «قال زيد عند التعجب: «وي»»، أو عند إناخة البعير «نخ»، أو «غاق» عند حكاية صوت الغراب،",
     "en": "And when they are uttered by way of reporting, as when you say “Zayd said, on wondering: ‘way’”, or, on making the camel kneel, “nikh”, or “ghāqi” on imitating the crow’s call,"},
    # REVIEW: the vowelling of «نخ» differs in this line («نخ» with kasra) from the earlier example (with fatḥa); vowels not reproduced per the no-diacritics rule.
    {"type": "matn",
     "ar": "فهي في هذه الحالة أيضا مبنية، لكن لا من حيث إنها أصوات، بل من حيث إنها حكاية عنها.",
     "en": "then in this case too they are indeclinable, but not insofar as they are sounds, rather insofar as they are reports of them."},
    {"type": "matn",
     "ar": "والمراد بالأصوات ههنا: ما كان باقية على ما هي عليه من غير نقلها على سبيل الحكاية[[٣]]، وهي بهذا الاعتبار ليست بأسماء، لعدم كونها دالة بالوضع،",
     "en": "What is meant by sound words here is what remains as it is, without being transferred by way of reporting; in this respect they are not nouns, since they do not signify by coinage (waḍʿ),…"},
    # REVIEW: «ما كان باقية» — masculine «كان» with feminine «باقية» as printed.

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "من تسكين البهيمة، أو حمله على الشرب، أو إناخته كما إذا قلت: نخ لإناخة البعير.",
     "en": "Such as calming the beast, urging it to drink, or making it kneel, as when you say “nakh” to make the camel kneel."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فهي داخلة في قوله: أو وقع غير مركب.",
     "en": "So they fall under his words “or it occurs uncombined”."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قال الفاضل الهندي: لأنه حينئذ اسم لصوت، وبه يشعر قوله: وهي بهذا الاعتبار ليست بأسماء،",
     "en": "Al-Fāḍil al-Hindī said: because it is then a noun for a sound; and his words “in this respect they are not nouns” hint at this."},
    {"type": "pair",
     "ar": "وله وجه ثان ذكره الفاضل الهندي، وهو أنه لا تفاوت حينئذ بين القسمين، فيقال: قال زيد نخ، ويقال: قال زيد غاق، فيصير القسمان قسما واحدا.",
     "en": "There is a second reason for it, mentioned by al-Fāḍil al-Hindī: that there is then no difference between the two kinds, for one says “Zayd said nakh” and one says “Zayd said ghāq”, so the two kinds become one."},
    {"type": "pair",
     "ar": "وفي الوجه الأول نظر؛ لأن المقصود من الصوت إحضاره بذاته إما ليحكم على المحضر أو ليطلب منه ما هو الغرض من صدوره كما هو في الألفاظ،",
     "en": "The first reason is open to question, because the purpose of a sound is to bring it to mind in itself, either so that something may be predicated of what is brought to mind, or so that what is intended by its utterance may be sought from it, as is the case with words;"},
    {"type": "pair",
     "ar": "وعلى كل تقدير فهو صوت، وليس باسم،",
     "en": "and on either supposition it is a sound and not a noun."},
    {"type": "pair",
     "ar": "لا يقال: يراد أنه اسم حكما، وفي أحكام الأسماء يعتبر اسم حقيقة أو حكما لأنا نقول: الأصوات مطلقا أسماء حكمية، ولذا عد قسما من الاسم المبني.",
     "en": "It should not be said: what is meant is that it is a noun by legal status, and in the rules of nouns a noun is considered whether real or by status; for we say: sound words in general are nouns by status, and that is why they are counted as a kind of indeclinable noun."},
    {"type": "pair",
     "ar": "وكذا في الثاني لأنه لا يلزم من عدم انقسامه إلى قسمين بهذا الاعتبار ألا يكون الأصوات معتبرة مطلقا بحيث لا يخرج عنها بهذا الاعتبار، ويكون انقسامه بغير هذا الاعتبار،",
     "en": "Likewise with the second, because its not dividing into two kinds in this respect does not entail that sound words are not considered absolutely, such that it does not leave them in this respect, its division being in some other respect."},
    {"type": "pair",
     "ar": "والحق أن المراد بالأصوات، وكذا كل قسم من أقسام المبني ما يشمل المراد به نفسه، والمستعمل لما هو الغرض منه،",
     "en": "The truth is that what is meant by sound words, and likewise by every kind of indeclinable, includes both what is meant as itself and what is used for its intended purpose;"},
    {"type": "pair",
     "ar": "وإلا لكان بيان المبنيات في الكتب النحوية قاصرا، وتعريف الأصوات يشمل كلها باعتبار الحكاية بها؛ لأنه يصدق على الجميع حكى به صوت.",
     "en": "otherwise the account of indeclinables in the books of grammar would be deficient. The definition of sound words includes all of them with respect to their being used to imitate, because “that by which a sound is imitated” is true of them all."},
]
