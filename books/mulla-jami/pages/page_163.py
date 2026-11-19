# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 163 (printed ١٦٢)."""

PAGE_NUMBER = 163
PRINTED_PAGE = "١٦٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "الفعل[[١]]، فإذا وجب التقدير، فالأصل أولى.",
     "en": "…the verb; so if estimation is necessary, the original [governor] is more fitting."},
    {"type": "matn",
     "ar": "ووجه الأقل: أنه خبره، والأصل في الخبر الإفراد[[٢]].",
     "en": "The reasoning of the minority: it is its khabar, and the rule for the khabar is singleness (ifrād)."},

    {"type": "section", "ar": "[ وجوب تقديم المبتدأ ]",
     "en": "When the Mubtadaʾ Must Come First (Wujūb Taqdīm al-Mubtadaʾ)"},

    {"type": "matn",
     "ar": "ثم إن الأصل في المبتدأ التقديم، وجاز تأخيره[[٣]]، لكنه قد يجب[[٤]] لعارض كما أشار إليه بقوله:",
     "en": "Further, the rule for the mubtadaʾ is precedence, and its postponement is permitted; but [precedence] may become necessary due to an incidental factor, as he indicated by his words:"},
    {"type": "matn",
     "ar": "(وإذا كان المبتدأ مشتملا[[٥]] على ما له صدر الكلام) أي: على معنى وجب له صدر الكلام[[٦]] كالاستفهام[[٧]]،",
     "en": "(And when the mubtadaʾ contains that which has the head of the utterance—ṣadr al-kalām), that is: a meaning for which the head of the utterance is required, such as interrogation;"},
    {"type": "matn",
     "ar": "فإنه يجب حينئذ تقديمه حفظا لصدارته (مثل: «من أبوك؟»)،",
     "en": "for then its being placed first is necessary, to preserve its initial position (ṣadāra), (as in: “Who is your father?”—man abūka?);"},
    {"type": "matn",
     "ar": "فإن «من» مبتدأ مشتمل على ما له صدر الكلام، وهو الاستفهام،",
     "en": "for “man” is a mubtadaʾ containing that which has the head of the utterance, namely interrogation;"},
    {"type": "matn",
     "ar": "فإن معناه: «أهذا أبوك أم ذاك؟» و«أبوك» خبره، وهذا مذهب سيبويه[[٨]].",
     "en": "for its meaning is: “Is this one your father, or that one?” and “abūka” is its khabar. This is the doctrine of Sībawayh."},
    {"type": "matn",
     "ar": "وذهب بعض النحاة[[٩]] إلى أن «أبوك» مبتدأ لكونه معرفة[[١٠]]، و«من» خبره الواجب",
     "en": "Some grammarians held that “abūka” is the mubtadaʾ because it is definite, and “man” is its khabar, which must…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "والقياس على نحو: \"الذي في الدار\"، و\"كل رجل في الدار\".",
     "en": "And [there is] analogy (qiyās) with such as “the one who is in the house” (alladhī fī al-dār) and “every man in the house.”"},
    {"type": "pair",
     "ar": "إن قيل: تقدير الجملة في المثالين للضرورة، ولا ضرورة فيما نحن فيه؟",
     "en": "If it is said: the estimation of a sentence in the two examples is by necessity, and there is no necessity in the case at hand?"},
    {"type": "pair",
     "ar": "قلنا: المتبادر إلى الذهن من الظرف المستقر معنى واحد، فإذا ثبت تقدير الجملة في بعض المواضع ثبت في الكل.",
     "en": "We say: what first comes to the mind from the settled adverbial (al-ẓarf al-mustaqarr) is a single meaning; so if the estimation of a sentence is established in some places, it is established in all."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ليتوافق الركنان.",
     "en": "So that the two pillars (rukn) [of the sentence] correspond."},
    {"type": "pair",
     "ar": "ولا يخفى أن عدم إفادة الزمان، والتقوي يقوي الإفراد.",
     "en": "It is not hidden that [the adverbial’s] not conveying time, and [the absence of] reinforcement (taqawwī), strengthen [the case for] singleness."},
    # REVIEW: the second clause «والتقوى يقوي الإفراد» is terse as printed; the bracketed «[the absence of]» is an interpretive supplement.

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "للاتساع وعدم التضييق كما هو مشرب العرب، ولهذا كان لغتهم أوسع اللغات.",
     "en": "For the sake of latitude and avoiding constraint, as is the way of the Arabs; and for this reason their language is the most expansive of languages."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الأحكام الخمسة كما تكون في الشرع تكون في النحو وغيره.",
     "en": "The five rulings (al-aḥkām al-khamsa), just as they exist in the sacred law, exist in grammar and elsewhere."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "اشتمال الدال على مدلوله سواء كانت دلالته بنفسه أو بما يجاوره من أمر متقدم عليه، نحو: «أزيد قائم؟» أو أمر متأخر عنه نحو: «غلام من جاءك؟»",
     "en": "[That is,] the containing of the signifier over its signified, whether its signification is by itself or by what adjoins it—something preceding it, as in “Is Zayd standing?” (a-Zaydun qāʾimun?), or something following it, as in “Whose servant came to you?” (ghulāmu man jāʾaka?)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: صدر داله أو صدر نفسه مسامحة.",
     "en": "That is: the head [position] of what signifies it—or “the head of itself,” by laxity of expression."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "وغيره من القسم، والتمني، والترجي، وضمير الشأن، ولام الابتداء، والشرط ولو بنوع تضمن، مثل: الذي يأتيني فله درهم.",
     "en": "And other [meanings]: the oath (qasam), wishing (tamannī), hoping (tarajjī), the pronoun of the matter (ḍamīr al-shaʾn), the lām of inception (lām al-ibtidāʾ), and the condition—even by a kind of implication—as in: “Whoever comes to me shall have a dirham.”"},
    {"type": "pair",
     "ar": "وبالجملة: ما يغير أصل الكلام، ويجعله نوعا آخر،",
     "en": "In sum: whatever alters the basic [form] of the utterance and makes it another kind."},
    {"type": "pair",
     "ar": "وإنما اقتضى التصدير؛ لأن السامع يبني الكلام الذي لم يصدر بالمغير على أصله،",
     "en": "It requires initial position only because the hearer construes an utterance not headed by the altering [element] according to its basic [form];"},
    {"type": "pair",
     "ar": "فلو جوز أن يجيء بعده ما يغيره لم يدر السامع إذا سمع بذلك المغير أهو راجع إلى ما قبله بالتغيير أو مغير لما سيجيء بعده من الكلام، فيتشوش بذلك ذهنه.",
     "en": "so were it allowed that what alters it might come after it, the hearer, on hearing that altering [element], would not know whether it bears back upon what precedes it by altering it, or alters what is yet to come after it in the utterance; and his mind would be confused by that."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "للإشارة إلى أنه المختار. لم يمثل المصنف بالمثال المتفق عليه، نحو: «من جاءك؟»",
     "en": "To indicate that it is the preferred [view]. The author did not illustrate with the agreed-upon example, such as “Who came to you?” (man jāʾaka?)."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "بل غير سيبويه.",
     "en": "Rather, [all] other than Sībawayh."},
    {"type": "pair",
     "ar": "قيل: لأن «من زيد؟» معناه: النجار أو الخياط مثلا، والوصف متعين للخبرية،",
     "en": "It is said: because the meaning of “Who is Zayd?” is, for example, “the carpenter or the tailor?”, and a descriptive is determined for [the role of] khabar."},
    {"type": "pair",
     "ar": "والمقدمة الأولى ممنوعة لصحة الإخبار بالكنى في الجواب، وكذا الثانية لصحة الإخبار عن الخياط بزيد.",
     "en": "The first premise is contested, since answering with kunyas (kunā) is valid; and likewise the second, since predicating “Zayd” of “the tailor” is valid."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "ولا يجوز تنكير المبتدأ مع تعريف الخبر.",
     "en": "And the mubtadaʾ may not be indefinite while the khabar is definite."},
    {"type": "pair",
     "ar": "نقل عن ابن الحاجب في دفعه: أن «من» معرفة؛ لأنه في قوة «أزيد أم عمرو أم خالد؟»،",
     "en": "It is reported from Ibn al-Ḥājib, in rebutting this, that “man” is definite, because it is equivalent to “Zayd, or ʿAmr, or Khālid?”;"},
    {"type": "pair",
     "ar": "وتطرق الإبهام في هذه المسميات على المتكلم لا يوجب لها تنكيرا. ولا يخفي ضعفه.",
     "en": "and the intrusion of vagueness regarding these named ones on the part of the speaker does not render them indefinite. Its weakness is not hidden."},
    {"type": "pair",
     "ar": "ونقل عن سيبويه جواز كون المبتدأ نكرة والخبر معرفة إذا كانت النكرة متضمنة",
     "en": "It is reported from Sībawayh that the mubtadaʾ may be indefinite and the khabar definite when the indefinite contains…"},
]
