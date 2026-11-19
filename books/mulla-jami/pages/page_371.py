# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 371 (printed ٣٧٠)."""

PAGE_NUMBER = 371
PRINTED_PAGE = "٣٧٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(منفصل مطابق للمبتدأ) إفرادا وتثنية» at the foot of PDF p. 370.
    {"type": "matn",
     "ar": "وجمعا، وتذكيرا وتأنيثا، وتكلما وخطابا وغيبة[[١]]",
     "en": "…and plural, in masculine and feminine, and in first, second and third person."},
    {"type": "matn",
     "ar": "(ويسمى) هذا المرفوع (فصلا) وذلك التوسط (ليفصل[[٢]]) ذلك المرفوع المتوسط (بين كونه) أي: كون الخبر (نعتا[[٣]] وخبرا) فيما يصلح لهما،",
     "en": "(It is called) — this nominative pronoun — (a separator) (faṣl), and that interposition is (so that it separates) — that interposed nominative pronoun — (between its being), that is, the predicate’s being, (an attribute and a predicate) in what is fit for both."},
    {"type": "matn",
     "ar": "ثم اتسع فأدخل فيه ما لا لبس فيه، وذلك عند اختلاف الإعراب، أو كون المبتدأ ضميرا، أو غير ذلك بالحمل على صورة اللبس.",
     "en": "Then the usage was widened, and what involves no ambiguity was admitted into it — that is, when the inflection differs, or when the subject is a pronoun, or the like — by assimilation to the case of ambiguity."},
    {"type": "matn",
     "ar": "(وشرطه) أي: شرط الفصل بذلك المرفوع (أن يكون الخبر معرفة)؛ لأن الفصل إنما يحتاج إليه فيها[[٤]]",
     "en": "(Its condition), that is, the condition of separation by that nominative pronoun, (is that the predicate be definite), because separation is needed only in that case,"},
    {"type": "matn",
     "ar": "(أو «أفعل من كذا»[[٥]]) لإلحاقه بالمعرفة لامتناع اللام",
     "en": "(or “afʿal min kadhā”) (more … than such-and-such), because it is classed with the definite noun, since the article is barred from it,"},
    {"type": "matn",
     "ar": "(مثل: «كان زيد هو أفضل من عمرو») واقتصر على مثال: «أفعل من»[[٦]] بعد دخول العوامل دون المعرفة ودون الخبر قبل العوامل لاستغنائها عن المثال، لكثرتهما.",
     "en": "(as in “kāna Zaydun huwa afḍala min ʿAmrin” (Zayd was more excellent than ʿAmr)). He confined himself to an example of “afʿal min” after the entry of the governors, and not of the definite noun, nor of the predicate before the governors, because these need no example, being so frequent."},
    {"type": "matn",
     "ar": "(ولا موضع له) أي: للفصل من الإعراب (عند الخليل[[٧]])؛ لأنه عنده حرف على صيغة الضمير،",
     "en": "(It has no position), that is, the separator has no position in inflection (maḥall min al-iʿrāb), (according to al-Khalīl), because in his view it is a particle in the form of a pronoun."},
    {"type": "matn",
     "ar": "وعند بعضهم: اسم مبني لا مقتضى فيه للإعراب، ولا عامل، لكن الخليل استبعد إلغاء الاسم، فذهب إلى حرفيته",
     "en": "According to some, it is an indeclinable noun in which there is nothing requiring inflection, and no governor; but al-Khalīl deemed it far-fetched for a noun to be left without function (ilghāʾ), so he held it to be a particle."},
    {"type": "matn",
     "ar": "(وبعض العرب يجعله مبتدأ[[٨]]) أي: يستعمله بحيث يحكم النحاة بكونه مبتدأ[[٩]]، وإلا فالعرب لا يعرف المبتدأ والخبر",
     "en": "(Some of the Arabs make it a subject), that is, they use it in such a way that the grammarians judge it to be a subject; otherwise, the Arabs do not know [the terms] subject and predicate…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ربما وقع بلفظ الغيبة بعد حاضر لقيامه مقام مضاف غائب.",
     "en": "It sometimes occurs in the third-person form after a present [first- or second-person] noun, because it stands in place of an absent annexed noun."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إشارة إلى أن قوله: ليفصل متعلق بقوله: يتوسط لا بقوله: يسمى فصلا.",
     "en": "This points out that his words “li-yafṣila” (so that it separates) are attached to his words “yatawassaṭu” (is interposed), not to his words “yusammā faṣlan” (is called a separator)."},
    # REVIEW: «بين كون المبتدأ نعتا وخبر» printed; the matn speaks of the predicate’s (الخبر) being an attribute, and «وخبرا» would be expected; transcribed as printed.
    {"type": "pair",
     "ar": "وذلك لأن اللام المقدرة بعدها أن لام كي، ومعناه سببية ما قبلها لما بعدها، والمسبب لفصله بين كون المبتدأ نعتا وخبر التوسط لا التسمية.",
     "en": "That is because the lām after which an is understood is the lām of purpose (lām kay), and its meaning is that what precedes it is the cause of what follows it; and what causes its separating between [the] being an attribute and a predicate is the interposition, not the naming."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قيل: يحتمل أن يكون حالا.",
     "en": "It has been said: it may be a circumstantial accusative (ḥāl)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فيما إذا كان المبتدأ على أصله، وهو التعريف،",
     "en": "That is, where the subject is in accordance with its basic state, which is definiteness."},
    {"type": "pair",
     "ar": "ولما لم يحتج إلى الفصل فيما هو الأصل من المبتدأ المعرفة للخبر النكرة حمل عليه ما احتيج إليه من المبتدأ النكرة، فلم يتوسط بينه وبين خبره ضمير الفصل.",
     "en": "Since the separator is not needed in what is the basic case — a definite subject with an indefinite predicate — the case in which it would be needed, an indefinite subject, was assimilated to it; so the separating pronoun is not interposed between it and its predicate."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أو فعلا مضارعا عند الزجاج تمسكا بقوله تعالى: «ومكر أولئك هو يبور» (فاطر:١٠)،",
     "en": "Or an imperfect verb (fiʿl muḍāriʿ), according to al-Zajjāj, who relies on the words of the Exalted: “and the plotting of those — it will perish” (Qurʾān, Sūrat Fāṭir 35:10)."},
    {"type": "pair",
     "ar": "ورد بأنه يحتمل كونه مبتدأ وتأكيدا كما في قوله تعالى: «وأنه هو أضحك وأبكى» (النجم:٤٣).",
     "en": "This was rejected on the ground that it may be a subject, or a corroborative (taʾkīd), as in the words of the Exalted: “and that it is He who makes [people] laugh and weep” (Qurʾān, Sūrat al-Najm 53:43)."},
    {"type": "pair",
     "ar": "وزيف بأن تأكيد الظاهر بالمضمر لم يعهد. ولا يخفى أن كلامه على السند الأخص.",
     "en": "That [rejoinder] was judged unsound on the ground that corroborating an explicit noun with a pronoun is not known. It is not hidden that his statement is directed at the more specific support (sanad)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أقول: اقتصر؛ لأن الدخول فيه مع الاستغناء عن الفصل كل استغناء، فيكون فيه إيضاح الغير بطريق الأولى.",
     "en": "I say: he confined himself [to it] because the entry [of the separator] occurs in it even though it has every means of dispensing with the separator; so it makes the other cases clear a fortiori."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "متعلق بقوله: له لأنه ظرف مستقر أو ظرف للنفي.",
     "en": "Attached to his word “lahu” (for it), because it is a ẓarf mustaqarr (an adverbial with an implied governor); or it is an adverbial of the negation."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "وبعضهم يجعله تأكيدا لما قبله، ويمنعه دخول لام التأكيد عليه، فإن لام التأكيد لا تدخل التأكيد.",
     "en": "Some make it a corroborative of what precedes it; this is ruled out by the entry of the lām of emphasis upon it, for the lām of emphasis does not enter upon a corroborative."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "لو كان معنى الجعل مبتدأ الحكم بكونه مبتدأ احتاج إلى هذا التوجيه.",
     "en": "If the meaning of “making it a subject” were judging it to be a subject, it would need this interpretation."},
    {"type": "pair",
     "ar": "وأما لو كان معناه كما هو الظاهر أنه يجعله في الاستعمال من أفراد المبتدأ، فلا يحتاج إلى هذا التوجيه؛ لأن جعل شيء متصفا بمفهوم شيء لا يتوقف على معرفة مفهوم ذلك الشيء.",
     "en": "But if its meaning, as is apparent, is that he makes it in usage one of the instances of the subject, it does not need this interpretation, because making a thing qualified by the concept of something does not depend on knowing the concept of that thing."},
]
