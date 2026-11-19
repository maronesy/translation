# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 48 (printed ٤٧)."""

PAGE_NUMBER = 48
PRINTED_PAGE = "٤٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "هند»، و«زيد قائم»، أو إنشائية[[١]]، مثل: «اضرب» و«لا تضرب»،",
     "en": "…Hind,” and “Zayd is standing (Zaydun qāʾimun),” or performative (inshāʾiyya), such as “Strike! (iḍrib)” and “Do not strike (lā taḍrib),”"},
    {"type": "matn",
     "ar": "فإن كل واحد منهما تضمن كلمتين، إحداهما: ملفوظة[[٢]]، والأخرى: منوية، وبينهما إسناد يفيد المخاطب[[٣]] فائدة[[٤]] تامة،",
     "en": "for each one of these two comprises two words: one of them uttered (malfūẓa) and the other intended but implicit (manwiyya), and between them is a predication that conveys to the addressee a complete benefit;"},
    {"type": "matn",
     "ar": "وحيث كانت الكلمتان[[٥]] أعم من أن تكونا كلمتين حقيقة أو حكما[[٦]]،",
     "en": "and since the “two words” are more general than that they be two words in reality or in ruling (ḥukman),"},
    {"type": "matn",
     "ar": "دخل في التعريف مثل: «زيد أبوه قائم»[[٧]]، أو «قام أبوه»[[٨]]، أو «قائم أبوه»[[٩]]، فإن الأخبار في هذه الجمل مع أنها مركبات[[١٠]] في حكم الكلمة المفردة[[١١]]، أعني: «قائم الأب»[[١٢]].",
     "en": "there enters under the definition [examples] such as “Zayd — his father is standing (Zaydun abūhu qāʾimun),” or “[Zayd] — his father stood (qāma abūhu),” or “[Zayd] — his father is standing (qāʾimun abūhu)”; for the predicates (akhbār) in these sentences — despite their being compounds — hold the ruling of a single word, I mean: “the-father-standing (qāʾimu al-ab).”"},
    {"type": "matn",
     "ar": "ودخل فيه أيضا مثل: «جسق مهمل»، و«ديز مقلوب زيد»، مع أن المسند إليه فيهما مهمل، ليس بكلمة، فإنه في حكم هذا اللفظ[[١٣]].",
     "en": "And there also enters under it [examples] such as “jasaq is meaningless,” and “dayz is the inversion of Zayd,” even though the subject (al-musnad ilayhi) in both is a meaningless [utterance], not a [proper] word — for it holds the ruling of this expression."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: غير محكية بها عن الواقع.",
     "en": "That is: [utterances] by which reality is not reported."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: ملفوظة حقيقة، والأخرى: منوية أي: ملفوظة حكما.",
     "en": "That is: uttered in reality; and the other: intended (manwiyya), that is: uttered in ruling."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الأولى: نسبة تفيد، إلى آخره.",
     "en": "It would be preferable [to say]: “a relation that conveys …,” to the end [of the phrase]."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الأولى أن يقال: بينهما نسبة يفيد المخاطب؛ لأن الإسناد معتبر فيه هذا الوصف، فبعد ذكر الإسناد لا حاجة إليه إلا أن يحمل على الصفة الكاشفة، وفيه بعد لا يخفى.",
     "en": "It would be preferable to say: “between them is a relation that conveys to the addressee,” because this attribute is already taken into account in predication; so after mentioning predication there is no need for it, unless it be construed as an explicative attribute (ṣifa kāshifa) — and in that there is a remoteness that is not hidden."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "هي تعليلية، أو مكانية، والأول أولى.",
     "en": "It [ḥaythu] is causal (taʿlīliyya) or locative (makāniyya), and the first is preferable."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يندرج في «حكما» ما يكون إحدى كلمتيه كلمة حكما.",
     "en": "There falls under “in ruling (ḥukman)” that in which one of its two words is a word only in ruling."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "مثال لكلام خبره جملة اسمية.",
     "en": "An example of a speech (kalām) whose predicate is a nominal sentence."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "عطف على «أبوه قائم»، مثال لكلام خبره جملة فعلية.",
     "en": "[It is] conjoined to “abūhu qāʾim”; an example of a speech whose predicate is a verbal sentence."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "عطف على «أبوه قائم»، مثال لكلام خبره مركب من اسم الفاعل وفاعله، واسم الفاعل مع فاعله ليس بجملة، بل مشبه بالجملة.",
     "en": "[It is] conjoined to “abūhu qāʾim”; an example of a speech whose predicate is composed of an active participle (ism al-fāʿil) and its agent — and an active participle together with its agent is not a sentence, but rather resembles a sentence."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "في كون الخبر في «زيد قائم أبوه» مركبا نظر؛ لأن الخبر عندهم هو «قائم»، وفاعله خارج عن الخبر.",
     "en": "In the predicate’s being a compound in “Zayd — his father is standing (Zaydun qāʾimun abūhu)” there is [room for] reflection, because the predicate according to them is only “qāʾim,” while its agent (fāʿil) lies outside the predicate."},
    {"type": "pair",
     "ar": "ولا يذهب عليك أن الأمثلة المذكورة داخلة في تعريف الكلام مع قطع النظر عن جعل الكلمتين أعم من الكلمتين حقيقة أو حكما.",
     "en": "And let it not escape you that the mentioned examples fall under the definition of speech irrespective of making “the two words” more general than two words in reality or in ruling."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "لأن النسبة في تلك المركبات مجملة، فيجوز التعبير عنها بما يفيد الإجمال، وهو المفرد.",
     "en": "Because the relation in those compounds is undifferentiated (mujmala), so it is permissible to express it by that which conveys undifferentiation — namely, the single word."},

    # ---------------- Footnote 12 ----------------
    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "ليس المقصود مجموع قائم الأب، فإنه مركب، وليس بكلمة، بل المراد القائم المضاف، والمضاف إليه خارج عنه.",
     "en": "What is meant is not the totality of “the-father-standing (qāʾim al-ab),” for that is a compound and not a [single] word; rather what is intended is “the standing one” as annexed term (al-muḍāf), while the term to which it is annexed (al-muḍāf ilayhi) lies outside it."},

    # ---------------- Footnote 13 ----------------
    {"type": "note", "num": "١٣"},
    {"type": "pair",
     "ar": "فلا يصح القول بأن الألفاظ موضوعة لأنفسها حتى يحتاج إلى هذا التأويل، لما حققه السيد الشريف من أن الألفاظ غير الدالة على أنفسها، بل هي تحضر بأنفسها في ذهن السامع، فيحكم عليها.",
     "en": "So it is not valid to hold that expressions are coined to denote themselves — such that recourse to this interpretation would be needed — because of what al-Sayyid al-Sharīf established: that expressions do not signify themselves; rather they themselves become present in the mind of the hearer, whereupon a judgement is made about them."},
    {"type": "pair",
     "ar": "ولئن سلمت دلالتها بالوضع لثبوته في الألفاظ المهملة.",
     "en": "And even if their signification by [linguistic] coinage (waḍʿ) be granted, [that would not help,] since it would then be established even for the meaningless expressions."},
]
