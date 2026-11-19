# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 162 (printed ١٦١)."""

PAGE_NUMBER = 162
PRINTED_PAGE = "١٦١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(وقد يحذف) العائد إذا كان ضميرا[[١]]، لقيام قرينة[[٢]]",
     "en": "(And it may be deleted)—the referent, when it is a pronoun—because a contextual indicator (qarīna) is present,"},
    {"type": "matn",
     "ar": "نحو: «البر الكر بستين درهما»، و«السمن منوان بدرهم» أي: «الكر منه» و«منوان منه»",
     "en": "as in: “Wheat—the kurr for sixty dirhams” (al-burru al-kurru bi-sittīna dirhaman), and “Ghee—two manns for a dirham” (al-samnu manawāni bi-dirhamin), that is: “the kurr of it” and “two manns of it,”"},
    {"type": "matn",
     "ar": "بقرينة أن بائع البر والسمن لا بسعر غيرهما.",
     "en": "by the indicator that [the price quoted by] the seller of wheat and ghee [is for them], not the price of anything else."},
    # REVIEW: printed «لا بسعر غيرهما» (one dot below: bāʾ); the sentence is elliptical as printed; transcribed exactly, English supplies the ellipsis in brackets.
    {"type": "matn",
     "ar": "(وما وقع ظرفا) أي: الخبر الذي وقع ظرف زمان أو مكان أو جارا ومجرورا[[٣]]",
     "en": "(And what occurs as an adverbial—ẓarfan), that is: the khabar that occurs as an adverbial of time or place, or as a preposition with its object,"},
    {"type": "matn",
     "ar": "(فالأكثر[[٤]]) من النحاة وهم البصريون[[٥]] على (أنه[[٦]])",
     "en": "(then most) of the grammarians—they are the Baṣrans—hold (that it),"},
    {"type": "matn",
     "ar": "أي: الخبر الواقع ظرفا (مقدر) أي: مؤول[[٧]] (بجملة) بتقدير الفعل فيه[[٨]]؛",
     "en": "that is, the khabar occurring as an adverbial, (is estimated—muqaddar), that is, interpreted (muʾawwal), (as a sentence), by estimating the verb in it;"},
    {"type": "matn",
     "ar": "لأنه إذا قدر فيه الفعل يصير جملة فعلية، بخلاف ما إذا قدر فيه اسم الفاعل، كما هو مذهب الأقل، وهم الكوفيون، فإنه يصير حينئذ مفردا.",
     "en": "because when the verb is estimated in it, it becomes a verbal sentence; unlike when the active participle is estimated in it, as is the doctrine of the minority—they are the Kūfans—for it then becomes a single [term] (mufrad)."},
    {"type": "matn",
     "ar": "وجه الأكثر: أن الظرف لا بد له من متعلق[[٩]] عامل فيه، والأصل في العمل هو",
     "en": "The reasoning of the majority: the adverbial must have a point of attachment (mutaʿallaq) that governs it, and the original [locus] of government is…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وأما غير الضمير، فكون الخبر عين المبتدأ لا يقبل الحذف،",
     "en": "As for what is other than the pronoun: the khabar’s being identical with the mubtadaʾ does not admit of deletion;"},
    {"type": "pair",
     "ar": "ووضع الظاهر موضع المضمر لنكتة تفوت مع الحذف.",
     "en": "and the placing of the overt noun in the position of the pronoun is for a subtle point (nukta) that is lost with deletion."},
    {"type": "pair",
     "ar": "وكذا لام العهد إذ مع الحذف لا ينساق الذهن إلا إلى الضمير.",
     "en": "Likewise the lām of prior reference; for with deletion the mind is led only to the pronoun."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "دل كلامه على أن الحذف شائع كلما قام قرينة، وليس كذلك",
     "en": "His words indicate that deletion is common whenever an indicator is present; but it is not so."},
    {"type": "pair",
     "ar": "بل خص ذلك بالضمير المجرور بـ«من» إذا كان في جملة اسمية يكون المبتدأ منها جزءا من مبتدئها.",
     "en": "Rather, that is restricted to the pronoun governed in the genitive by “min,” when it is in a nominal sentence whose mubtadaʾ is a part of the [first] mubtadaʾ."},
    {"type": "pair",
     "ar": "وأما في غيرها ففي المرفوع لا يجوز الحذف، والمنصوب والمجرور سماعي.",
     "en": "As for elsewhere: in the nominative, deletion is not permitted; and [deletion of] the accusative and the genitive depends on attested usage (samāʿī)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لا يخفى أن الظرف هو اسم الزمان والمكان، وإطلاقه على الجار والمجرور الذي ليس بزمان ولا بمكان بطريق المجاز،",
     "en": "It is not hidden that the ẓarf is the noun of time and place, and that its application to the preposition and its object that is neither time nor place is by way of figurative usage (majāz);"},
    {"type": "pair",
     "ar": "فمن إرادة المجموع يلزم الجمع بين الحقيقة والمجاز،",
     "en": "so intending the whole entails combining the literal (ḥaqīqa) and the figurative,"},
    {"type": "pair",
     "ar": "إلا أن يقال بعموم المجاز بأن يراد معنى مجازي شامل لجميعها.",
     "en": "unless one speaks of a generalized figurative sense (ʿumūm al-majāz), such that a figurative meaning comprehending all of them is intended."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الفاء لتضمن المبتدأ معنى الشرط، فإن «ما» في ما وقع موصولة أو موصوفة.",
     "en": "The fāʾ is because the mubtadaʾ contains the sense of a condition; for “mā” in “mā waqaʿa” is a relative (mawṣūla) or an indefinite qualified [noun] (mawṣūfa)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فيه أنه لو كان هذا مذهب البصريين، فالمناسب أن يقال: وما وقع ظرفا فهو مقدر بجملة خلافا للكوفيين؛",
     "en": "There is [an objection] here: had this been the doctrine of the Baṣrans, it would have been fitting to say: “What occurs as an adverbial is estimated as a sentence, contrary to the Kūfans”;"},
    {"type": "pair",
     "ar": "لأن المصنف تابع للبصريين، ويذكر مذهب البصريين، وينقل الخلاف لو وقع من واحد.",
     "en": "because the author follows the Baṣrans: he states the doctrine of the Baṣrans and reports the disagreement if it arises from anyone."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أشار إلى تقدير الجار ليرتبط بالمبتدأ، أي: قوله: فالأكثر.",
     "en": "He indicated the estimation of the preposition [ʿalā] so that it would be linked to the mubtadaʾ, that is, to his words “fa-l-akthar.”"},
    {"type": "pair",
     "ar": "ويجوز تقدير المضاف لهذا الربط بأن يقال: فحكم الأكثر أنه مقدر بجملة.",
     "en": "It is also permissible to estimate a governing noun (muḍāf) for this linking, by saying: “The ruling of the majority is that it is estimated as a sentence.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "فسر التقدير بالتأويل؛ لأن التقدير يوهم أن يقدر الجملة في نظم الكلام، فيلزم أن تكون الجملة محذوفة، وليس كذلك،",
     "en": "He explained “estimation” (taqdīr) as “interpretation” (taʾwīl), because “estimation” suggests that the sentence is estimated within the arrangement of the speech, so that the sentence would have to be deleted; but it is not so."},
    {"type": "pair",
     "ar": "بل الخبر الجملة هو نفس هذا الظرف، واعتبار الفعل من حيث ارتباط الظرف به لا يوجب الحذف بنفس هذا الظرف بتأويل هذه الجملة.",
     "en": "Rather, the sentence-khabar is this adverbial itself; and taking the verb into account inasmuch as the adverbial is linked to it does not necessitate deletion, the adverbial itself being interpreted as this sentence."},
    {"type": "pair",
     "ar": "ويجوز أن يراد التعيين كما يقال: الفروض المقدرة في كتاب الله أي: المعينة في كتاب الله.",
     "en": "It is also possible that “determination” (taʿyīn) is meant, as one says: “the shares estimated (al-muqaddara) in the Book of Allah,” that is, “determined in the Book of Allah.”"},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "وذلك الفعل من أفعال العموم غالبا، كالكون والثبوت والحصول والوجود.",
     "en": "That verb is usually one of the general verbs (afʿāl al-ʿumūm), such as being, being established, occurring and existing."},
    {"type": "pair",
     "ar": "ويجوز تقدير فعل من أفعال الخصوص عند قرينة.",
     "en": "It is permissible to estimate one of the specific verbs (afʿāl al-khuṣūṣ) when there is an indicator."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "قيل: اتفق النحاة على ذلك.",
     "en": "It is said: the grammarians agree on this."},
    {"type": "pair",
     "ar": "وفيه بحث: لأن الظرف لا بد له من مظروف، والمظروف في «زيد في الدار» هو «زيد»، ولا حاجة إلى أمر آخر هذا؟",
     "en": "This is open to discussion: for an adverbial must have something it contains (maẓrūf), and the contained in “Zayd is in the house” is “Zayd”; so what need is there for another thing besides this?"},
    {"type": "pair",
     "ar": "قلت: الظرف يكون ظرفا لأمر من أمور «زيد» من قيامه أو سكونه أو حصوله أو غير ذلك، فلا بد من تقديره ليتم البيان.",
     "en": "I say: the adverbial is the container of one of the matters pertaining to “Zayd”—his standing, his being at rest, his being present, or the like—so it must be estimated for the exposition to be complete."},
]
