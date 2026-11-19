# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 345 (printed ٣٤٤)."""

PAGE_NUMBER = 345
PRINTED_PAGE = "٣٤٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «هذا حاصل ما ذكره المصنف في شرحه.» at the foot of PDF p. 344 (new sentence).
    {"type": "matn",
     "ar": "(وهو) أي: التأكيد (لفظي[[١]]) أي: منسوب إلى اللفظ لحصوله من تكرير اللفظ (ومعنوي[[٢]]) أي: منسوب إلى المعنى لحصوله من ملاحظة المعنى.",
     "en": "(It), that is, the corroborative, (is verbal [lafẓī]), that is, related to the wording, because it arises from repeating the word, (and semantic [maʿnawī]), that is, related to the meaning, because it arises from attention to the meaning."},
    {"type": "matn",
     "ar": "(فاللفظي) منه: (تكرير اللفظ الأول) أي: مكرر اللفظ الأول ومعاده حقيقة (مثل: «جائني زيد زيد») أو حكما نحو: «ضربت أنت، وضربت أنا»،",
     "en": "(The verbal) kind of it (is the repetition of the first word), that is, the first word repeated and restated, either in reality, (as in “jāʾanī Zaydun Zaydun”) (Zayd, Zayd came to me), or by status, as in “ḍarabta anta” (you struck, you) and “ḍarabtu anā” (I struck, I);"},
    {"type": "matn",
     "ar": "فإن ذلك في حكم تكرير اللفظ، وإن كان مخالفا للأول لفظا؛ إذ الضرورة داعية إلى المخالفة؛ لأنه لا يجوز تكريره متصلا[[٣]].",
     "en": "for that has the status of repeating the word, even though it differs from the first in wording, since necessity calls for the difference: it is not permitted to repeat it as a connected [pronoun]."},
    {"type": "matn",
     "ar": "(ويجري) أي: التكرير مطلقا، لا التكرير الذي هو التأكيد الاصطلاحي (في الألفاظ كلها[[٤]]) أسماء أو أفعالا أو حرفا أو جملا أو مركبات تقييدية أو غير ذلك،",
     "en": "(It occurs), that is, repetition in general, not the repetition that is the technical corroborative, (in all words), whether nouns, verbs, a particle, sentences, restrictive compounds (murakkabāt taqyīdiyya) or otherwise."},
    {"type": "matn",
     "ar": "ولا يبعد إرجاع الضمير إلى التأكيد اللفظي[[٥]] الاصطلاحي وتخصيص الألفاظ بالأسماء، ويكون المقصود من هذا التعميم عدم اختصاصه بألفاظ محصورة كالتأكيد المعنوي.",
     "en": "It is not far-fetched to refer the pronoun to the technical verbal corroborative and to restrict “words” to nouns; the purpose of this generalization would then be that it is not confined to a limited set of words, as the semantic corroborative is."},
    {"type": "matn",
     # REVIEW: «أبصع» (with ṣād) printed here in the matn; footnote ٦ prints «أبضع» (with ḍād). Each transcribed as printed.
     "ar": "(و) التأكيد (المعنوي) مختص (بألفاظ محصورة) أي: معدودة محدودة (وهي: «نفسه»، و«عينه»[[٦]]، و«كلاهما»، و«كله»، و«أجمع»، و«أكتع»، و«أبتع»، و«أبصع»)",
     "en": "(And the semantic) corroborative is confined (to a limited set of words), that is, counted and defined, (namely “nafsuhu” [himself], “ʿaynuhu” [himself], “kilāhumā” [both of them], “kulluhu” [all of it], “ajmaʿ”, “aktaʿ”, “abtaʿ” and “abṣaʿ” [all, entire]) …"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "مختص بالمعارف إلا في المحكوم به.",
     "en": "It is confined to definite nouns, except in what is predicated (al-maḥkūm bihi)."},
    {"type": "pair",
     "ar": "وكذا المعنوي مختص بالمعارف مطلقا عند البصريين، ونفسه وعينه منه عند الكوفيين.",
     "en": "Likewise the semantic [corroborative] is confined to definite nouns without qualification according to the Baṣrans, and “nafsuhu” and “ʿaynuhu” [alone] of it according to the Kūfans."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لا يجوز أن تؤكد النكرة بالتأكيد اللفظي إلا إذا كانت تلك النكرة محكوما بها، ولا تؤكد بالمعنوي مطلقا عند البصريين.",
     "en": "An indefinite noun may not be corroborated by the verbal corroborative unless that indefinite noun is predicated, and according to the Baṣrans it is never corroborated by the semantic corroborative."},
    {"type": "pair",
     "ar": "وأما الكوفيون فيجوزون التأكيد بكل وأجمع دون نفسه وعينه إذا كانت النكرة معلومة المقدار كدرهم ويوم وشهر.",
     "en": "The Kūfans, however, permit corroboration by “kull” and “ajmaʿ”, but not by “nafsuhu” and “ʿaynuhu”, when the indefinite noun is of known measure, such as “dirham”, “day” and “month”."},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: ذلك ليس ببعيد.",
     "en": "Shaykh al-Raḍī said: that is not far-fetched."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قصد به الفرق بين ضربت أنا وأجمع وأكتع، فإن الأول في حكم التكرير لفظا؛ لأن المخالفة للضرورة بخلاف أجمع وأبتع،",
     "en": "By this he intended the distinction between “ḍarabtu anā” and “ajmaʿ” and “aktaʿ”: the first has the status of verbal repetition, because the difference is due to necessity, unlike “ajmaʿ” and “abtaʿ”."},
    {"type": "pair",
     "ar": "ومنهم من لم ينبه لغرضه. واعترض بعدم الفرق بين ضربت أنا وأجمع وأكتع.",
     "en": "Some did not notice his purpose, and objected that there is no distinction between “ḍarabtu anā” and “ajmaʿ” and “aktaʿ”."},
    {"type": "pair",
     "ar": "اعلم أن من قال: إن الضمير في أنت هو التاء، وأنه عماد، فالتأكيد في ضربت أنت وأخواته بتكرير اللفظ الأول حقيقة.",
     "en": "Know that for whoever says that the pronoun in “anta” is the tāʾ and that [an-] is a support (ʿimād), the corroboration in “ḍarabta anta” and its sisters is by repetition of the first word in reality."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "اعلم أن المؤكد إما مستقل يجوز الابتداء به والوقف عليه، أو غير مستقل،",
     "en": "Know that the word corroborated is either independent, such that one may begin with it and pause on it, or not independent."},
    {"type": "pair",
     "ar": "فغير المستقل إن كان على حرف واحد أو كان مما يجب اتصاله بأول نوع من الكلم أو بآخر نوع منها تكرر بتكرير عماده في السعة نحو: بك بك، وضربت ضربت،",
     "en": "If the non-independent consists of a single letter, or is among what must be joined to the beginning or the end of some kind of word, it is repeated, in unconstrained usage (al-saʿa), by repeating its support, as in “bika bika” (by you, by you) and “ḍarabtu ḍarabtu” (I struck, I struck);"},
    {"type": "pair",
     "ar": "وإن لم يكن على حرف واحد ولا واجب الاتصال جاز تكريره وحده نحو: إن إن زيدا قائم.",
     "en": "if it does not consist of a single letter and need not be joined, it may be repeated alone, as in “inna inna Zaydan qāʾimun” (truly, truly Zayd is standing)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قلت: على أي تقدير يشكل بأجمع وأخواته، فإنه لا يجري فيها التأكيد اللفظي،",
     "en": "I say: on either supposition, it is problematic with “ajmaʿ” and its sisters, for the verbal corroborative does not occur in them."},
    {"type": "pair",
     "ar": "ودفعه بتأويل الشمول المستفاد من كلها بالشمول للأنواع لا لجميع الأشخاص.",
     "en": "It is answered by interpreting the comprehensiveness conveyed by “kullihā” (all of them) as comprehensiveness of the kinds, not of all individual items."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وقد يزاد الباء في عينه، وكذا في أجمع، فيضاف إلى ضمير المؤكد،",
     "en": "The bāʾ is sometimes added in “ʿaynihi”, and likewise in “ajmaʿ”, which is then annexed to the pronoun of the word corroborated."},
    {"type": "pair",
     "ar": "وقد نبه المصنف على ترتيب ألفاظ التوكيد إذا جمع، لكن الجمهور على تقديم أبضع على أبتع، والزمخشري منفرد في تقديم أبتع، والمصنف تبعه.",
     "en": "The author drew attention to the order of the corroborative words when they are combined; but the majority place “abḍaʿ” before “abtaʿ”; al-Zamakhsharī alone places “abtaʿ” first, and the author followed him."},
]
