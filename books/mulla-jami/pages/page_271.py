# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 271 (printed ٢٧٠)."""

PAGE_NUMBER = 271
PRINTED_PAGE = "٢٧٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(والثاني) أي: القسم الثاني من التمييز، وهو ما يرفع الإبهام عن ذات مقدرة يرفعه» from the foot of PDF p. 270.
    {"type": "matn",
     "ar": "(عن نسبة) كان الظاهر أن يقول[[١]]: عن ذات مقدرة في نسبة في جملة،",
     "en": "…(from a relation). The obvious [wording] would have been for him to say: “from an implied entity (dhāt muqaddara) in a relation in a sentence”;"},
    {"type": "matn",
     "ar": "لكن لما كان الإبهام في طرف النسبة يستلزم الإبهام فيها[[٢]]، ورفعه عنها يستلزم الرفع عنه، قال: «عن نسبة» مقتصرا عليها،",
     "en": "but since indefiniteness (ibhām) in a term of the relation entails indefiniteness in it [the relation], and removing it from [the relation] entails removing it from [the term], he said “from a relation,” confining himself to it,"},
    {"type": "matn",
     "ar": "تنبيها على أن مقابلة ما في هذا القسم للمفرد المذكور في القسم الأول إنما هي بمجرد النسبة لا غير",
     "en": "to point out that the contrast between what is in this division and the single word (mufrad) mentioned in the first division lies solely in the relation and nothing else."},
    {"type": "matn",
     "ar": "(في جملة) أي: نسبة كائنة في جملة (أو ما ضاهاها) أي: ما شابهها، عطف على «جملة»، وهو:",
     "en": "(In a sentence), that is, a relation found in a sentence, (or what resembles it), that is, what is similar to it—coordinated with “sentence”—and that is:"},
    {"type": "matn",
     "ar": "١-اسم الفاعل: نحو: «الحوض ممتلئ ماء».",
     "en": "1. The active participle (ism al-fāʿil), as in “The basin is full of water.”"},
    {"type": "matn",
     "ar": "٢-أو اسم المفعول: نحو: «الأرض مفجرة عيونا».",
     "en": "2. Or the passive participle (ism al-mafʿūl), as in “The earth is burst open with springs.”"},
    {"type": "matn",
     "ar": "٣-أو الصفة المشبهة: نحو: «زيد حسن وجها».",
     "en": "3. Or the qualificative adjective (al-ṣifa al-mushabbaha), as in “Zayd is handsome of face.”"},
    {"type": "matn",
     "ar": "٤-أو اسم التفضيل: نحو: «زيد أفضل أبا».",
     "en": "4. Or the elative (ism al-tafḍīl), as in “Zayd is more excellent in respect of father.”"},
    {"type": "matn",
     "ar": "٥-أو المصدر[[٣]]: نحو: «أعجبني طيبه أبا».",
     "en": "5. Or the verbal noun (maṣdar), as in “His goodness in respect of father pleased me.”"},
    {"type": "matn",
     "ar": "٦-وكذا كل ما فيه معنى الفعل[[٤]]: نحو: «حسبك زيد[[٥]] رجلا».",
     "en": "6. Likewise everything that carries the meaning of the verb, as in “Zayd suffices you as a man.”"},
    {"type": "matn",
     "ar": "(نحو: طاب زيد نفسا) مثال للجملة، والتمييز فيه خاص بالمنتصب عنه.",
     "en": "(As in “Zayd is good in soul”): an example of the sentence; the specification (tamyīz) in it is particular to that from which it takes the accusative."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لأن الإبهام الذي يستدعي التمييز ليس إلا في الذات المقدرة التي هي طرف النسبة،",
     "en": "Because the indefiniteness that calls for a specification lies only in the implied entity which is a term of the relation;"},
    {"type": "pair",
     "ar": "لكن لما كان ذلك الإبهام مستلزما لنوع إبهام في النسبة حسب احتمالات الطرف، ورفع إبهامها التبعي مستلزما لرفع إبهام الطرف صح قوله عن نسبة،",
     "en": "but since that indefiniteness entails a kind of indefiniteness in the relation according to the possibilities of the term, and removing its derivative indefiniteness entails removing the indefiniteness of the term, his words “from a relation” are correct."},
    {"type": "pair",
     "ar": "والنكتة فيه التنبيه على أن مقابلة هذا القسم للقسم السابق باعتبار أن ليس هناك نسبة كذلك لا باعتبار عدم ذكر الذات هنا، وذكرها في السابق.",
     "en": "The subtle point (nukta) in it is to indicate that this division contrasts with the preceding division in that there is no such relation there, not in that the entity is unmentioned here and mentioned in the preceding one."},
    {"type": "pair",
     "ar": "ألا ترى أن «نعم رجلا» مندرج في القسم الأول مع أن الضمير غير مذكور.",
     "en": "Do you not see that “What an excellent man!” (niʿma rajulan) falls under the first division, although the pronoun is not mentioned?"},
    {"type": "pair",
     "ar": "هذا حاصل كلامه قدس سره.",
     "en": "This is the gist of his words, may his secret be sanctified."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الإبهام في طرف النسبة لا يستلزم إبهاما فيها يرفع القسم الثاني من التمييز.",
     "en": "Indefiniteness in a term of the relation does not entail an indefiniteness in [the relation] that the second division of specification removes."},
    {"type": "pair",
     "ar": "ألا يرى أن قولنا: عندي رطل لا إبهام في النسبة فيه إنما الإبهام في الطرف.",
     "en": "Does one not see that in our saying “I have a raṭl” there is no indefiniteness in the relation; the indefiniteness is only in the term?"},
    {"type": "pair",
     "ar": "وبإزالة الإبهام عن النسبة لا يزول الإبهام عن الطرف، وبإزالة الإبهام عن الطرف لا يزول الإبهام عن النسبة نحو: «طاب رطل زيتا»، فإن النسبة فيها على إبهامها،",
     "en": "By removing the indefiniteness from the relation the indefiniteness is not removed from the term, and by removing the indefiniteness from the term the indefiniteness is not removed from the relation, as in “A raṭl was good in respect of oil,” for the relation in it remains indefinite."},
    {"type": "pair",
     "ar": "فكل من الحكمين أعني: قوله: الإبهام في طرف النسبة يستلزم الإبهام فيها. وقوله: ورفعه عنها يستلزم الرفع عنه محل بحث إلا أن يراد الطرف المقدر.",
     "en": "So each of the two judgements—I mean his statement “indefiniteness in a term of the relation entails indefiniteness in it,” and his statement “and removing it from it entails removing it from [the term]”—is open to discussion, unless the implied term is meant."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    # REVIEW: the first «ولهذ» is printed without the final alif (for «ولهذا»); transcribed as printed.
    {"type": "pair",
     "ar": "جعله الشيخ الرضي داخلا في شبه الجملة. ولهذ قال: لا حاجة إلى قوله: أو في إضافة،",
     "en": "Shaykh al-Raḍī made it fall under the quasi-sentence (shibh al-jumla); for this reason he said: there is no need for his words “or in a genitive construction (iḍāfa).”"},
    {"type": "pair",
     "ar": "لكن المصنف لم يجعله من هذا القسم. ولهذا قال: أو في إضافة.",
     "en": "But the author did not make it part of this division; for this reason he said: “or in a genitive construction.”"},
    {"type": "pair",
     "ar": "لعله أراد بشبه الجملة ما يشتمل على نسبة قريبة من النسبة التامة، وليست الإضافة كذلك.",
     "en": "Perhaps by “quasi-sentence” he meant what contains a relation close to the complete relation, and the genitive construction is not so."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يشكل بأسماء الأفعال، فإن فيها معنى الفعل، وليست بشبه جملة، بل جملا.",
     "en": "This is problematic in the case of verbal nouns of command (asmāʾ al-afʿāl), for they carry the meaning of the verb, yet they are not quasi-sentences but sentences."},
    {"type": "pair",
     "ar": "واعلم أن في قوله: وهو اسم الفاعل إلى آخره مسامحة. والمراد هو اسم الفاعل مع فاعله.",
     "en": "Know that in his words “and that is the active participle…” to the end there is laxity of expression; what is meant is the active participle together with its agent."},
    # REVIEW: «وهكذا وينبغي» printed with both words; transcribed as printed.
    {"type": "pair",
     "ar": "وهكذا وينبغي أن يخص اسم الفاعل والمفعول والصفة المشبهة أيضا بما ليست جملا ذكرتها لك جملا رجاء ألا يخفى على نحوك.",
     "en": "And so on. The active participle, the passive participle and the qualificative adjective should also be restricted to those that are not sentences; I have mentioned them to you as sentences in the hope that [this] will not be hidden from one like you."},
    {"type": "pair",
     "ar": "والأولى في قوله: حسبك زيد رجلا، حسبك رجلا زيد؛ لأن حسبك زيد جملة، وشبهها حسبك، فالممثل به هو التمييز من حسبك لا من حسبك زيد.",
     "en": "Better, in his example “ḥasbuka Zaydun rajulan,” would be “ḥasbuka rajulan Zaydun”; for “ḥasbuka Zaydun” is a sentence, and its quasi-sentence is “ḥasbuka,” so what is exemplified is the specification of “ḥasbuka,” not of “ḥasbuka Zaydun.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: يكفيك زيد.",
     "en": "That is: Zayd suffices you."},
]
