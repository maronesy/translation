# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 196 (printed ١٩٥)."""

PAGE_NUMBER = 196
PRINTED_PAGE = "١٩٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # continues from page 195 ("…إن الفعل واقع عليه،")
    {"type": "matn",
     "ar": "بل فيه أو له أو معه،",
     "en": "…but rather “in it,” “for it” or “with it”;"},
    {"type": "matn",
     "ar": "والمفعول المطلق مما يفهم من مغايرته[[١]] لفعل الفاعل، فإن المفعول المطلق عين فعله.",
     "en": "and the absolute object [is excluded] by what is understood from its being distinct from the agent’s act, for the absolute object is the very act of the agent."},
    {"type": "matn",
     "ar": "والمراد بفعل الفاعل: فعل اعتبر إسناده[[٢]] إلى ما هو فاعله حقيقة أو حكما.",
     "en": "What is meant by “the act of the agent” is an act whose predication to what is its agent, really or by legal status (ḥukman), is taken into account."},
    {"type": "matn",
     "ar": "فخرج به مثل «زيد» في «ضرب زيد»[[٣]] على صيغة المجهول، فإنه لم يعتبر إسناده إلى فاعله.",
     "en": "By this is excluded the like of “Zayd” in “ḍuriba Zaydun” (Zayd was struck), in the passive form, for its predication to its agent is not taken into account."},
    {"type": "matn",
     "ar": "ولا يشكل بمثل: «أعطي زيد درهما»، فإنه يصدق على «درهما» أنه ما وقع عليه فعل الفاعل الحكمي المعتبر إسناد الفعل إليه، فإن مفعول ما لم يسم فاعله في حكم الفاعل.",
     "en": "No difficulty is raised by the like of “uʿṭiya Zaydun dirhaman” (Zayd was given a dirham), for it holds true of “dirhaman” that it is what the act of the agent-by-status falls upon, the predication of the act to which is taken into account; for the object of a verb whose agent is not named (mafʿūl mā lam yusamma fāʿiluhu) has the status of the agent."},
    {"type": "matn",
     "ar": "وبما ذكرنا ظهر فائدة ذكر الفاعل، فلا يرد[[٤]] أنه لو قال: «ما وقع عليه الفعل» لكان أخصر.",
     "en": "From what we have said the benefit of mentioning “the agent” is clear; so the objection does not hold that, had he said “what the act falls upon,” it would have been more concise."},
    {"type": "matn",
     "ar": "(نحو: ضربت زيدا)، فإن «زيدا» قد وقع عليه بلا وساطة حرف جر فعل اعتبر إسناده إلى الفاعل الذي هو ضمير المتكلم.",
     "en": "(As in: “ḍarabtu Zaydan”), for upon “Zaydan” there has fallen, without the mediation of a preposition, an act whose predication to the agent—the first-person pronoun—is taken into account."},
    {"type": "matn",
     "ar": "(وقد يتقدم) المفعول به[[٥]] (على الفعل) العامل فيه، لقوة الفعل[[٦]] في العمل، فيعمل فيه متقدما ومتأخرا[[٧]]:",
     "en": "(And) the direct object (may precede the verb) that governs it, because of the strength of the verb in governing, so that it governs it whether [the object is] placed before or after:"},
    {"type": "matn",
     "ar": "إما جوازا[[٨]]: مثل: «الله أعبد» و«وجه الحبيب أتمنى».",
     "en": "either optionally, as in: “Allāha aʿbudu” (Allah I worship) and “wajha al-ḥabībi atamannā” (the beloved’s face I long for)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لا حاجة إلى هذا الاعتبار لإخراجه؛ لأنه لا يقال: الضرب وقع الضرب أو الضربة، بل يقال: وقع الضرب أو الضربة.",
     "en": "There is no need for this consideration to exclude it, because one does not say “the striking—the striking or the blow fell [on it],” but rather one says “the striking or the blow occurred.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الأولى فعل أسند، وكذا الأولى في قوله: فإنه لم يعتبر إسناده لم يسند.",
     "en": "Better would be “an act that is predicated”; likewise, in his words “for its predication is not taken into account,” better would be “it is not predicated.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الأولى أن يقال: فخرج به زيد، ودخل درهما في «أعطي زيد درهما»،",
     "en": "Better would be to say: “By this ‘Zayd’ is excluded and ‘dirhaman’ in ‘uʿṭiya Zaydun dirhaman’ is included,”"},
    {"type": "pair",
     "ar": "وإخراج «زيد» إنما يتم لو لم يكن مفعول به في اصطلاحهم، وهو الأرجح الأليق بالاعتبار ما لم يوجد منهم تصريح بأنه مفعول به.",
     "en": "though excluding “Zayd” holds only if it is not a direct object in their terminology; and that is the more probable and the more fitting to consider, so long as no explicit statement is found from them that it is a direct object."},
    {"type": "pair",
     "ar": "وقولهم: بأن المفعول به وفيه يصح أن يكونا مفعولي ما لم يسم فاعله لا يدل على تسمية مفعول ما لم يسم فاعله مفعولا به أو مفعولا فيه كما لا يخفى.",
     "en": "Their saying that the direct object and the adverbial object (mafʿūl fīhi) can both serve as the object of a verb whose agent is not named does not indicate that the object of such a verb is called a direct object or an adverbial object, as is not hidden."},
    {"type": "pair",
     "ar": "فمن منع عدم كونه مفعولا به خفي عليه المانع لدقته.",
     "en": "So whoever denies that it is not a direct object, the impediment has escaped him because of its subtlety."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لعل المورد نظر إلى أنه مفعول به، لكنه مرفوع.",
     "en": "Perhaps the one raising [the objection] considered that it is a direct object, only in the nominative."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وكذا سائر المفاعيل سوى المفعول معه لمراعاة أصل الواو، فإنها في الأصل للعطف، وموضعها أثناء الكلام.",
     "en": "Likewise all the other objects except the concomitant object (al-mafʿūl maʿahu), out of regard for the original [function] of the wāw: originally it is for coordination, and its place is in the middle of speech."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "نبه على أن ذكر الفعل هنا ليس من قبيل الاكتفاء بما هو الأصل، كما في نظائره، لكن ينبغي أن يعلم أن اسم الفاعل والمفعول كالفعل.",
     "en": "He drew attention to the fact that mentioning “the verb” here is not a case of contenting oneself with what is primary, as in its parallels; but it should be known that the active and passive participles are like the verb."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "حالان من الفاعل أو المفعول، أو خبران لـ«كان» المحذوف، واسمه راجع إلى الفعل أو المفعول.",
     "en": "[Mutaqaddiman and mutaʾakhkhiran are] two ḥāls of the agent or of the object, or two predicates of an elided “kāna,” whose subject refers to the verb or the object."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "إشارة إلى أن تقدم المفعول على الفعل بأحد الوجوه الثلاثة: إما جائزا، وإما واجب، وإما ممتنع.",
     "en": "An indication that the object’s preceding the verb is in one of three ways: either permitted, or obligatory, or prohibited."},
    # REVIEW: print has «إما جائزا، وإما واجب، وإما ممتنع» (accusative then nominatives); transcribed as printed.
]
