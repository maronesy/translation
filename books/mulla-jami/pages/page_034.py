# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 34 (printed ٣٣)."""

PAGE_NUMBER = 34
PRINTED_PAGE = "٣٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "كان أو موضوعا[[١]]، مفردا كان أو مركبا[[٢]].",
     "en": "[whether used] or coined (mawḍūʿ), and whether simple (mufrad) or compound (murakkab)."},
    {"type": "matn",
     "ar": "واللفظ الحقيقي[[٣]]: ك«زيد» و«ضرب»[[٤]]، والحكمي: كالمنوي في «زيد ضرب» و«اضرب»؛ إذ ليس من مقولة الحرف والصوت[[٥]] أصلا، ولم يوضع له[[٦]] لفظ[[٧]].",
     "en": "The real utterance (al-lafẓ al-ḥaqīqī) is like “Zayd” and “ḍaraba”; and the constructive one (al-ḥukmī) is like the implied pronoun (al-manwī) in “Zaydun ḍaraba” and “iḍrib” — since it is not of the category of letter and sound (ḥarf wa-ṣawt) at all, and no utterance has been coined for it."},
    {"type": "matn",
     "ar": "وإنما عبروا عنه[[٨]] باستعارة لفظ المنفصل له من نحو: «هو»[[٩]] و«أنت»، وأجروا عليه[[١٠]]",
     "en": "They expressed it only by borrowing for it the detached (munfaṣil) pronoun, such as “huwa” and “anta,” and they applied to it"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "المشهور في كلام النحاة: مهملا كان أو مستعملا. وإنما عدل عن المهمل؛ لأن المهمل ما لم يوضع، وهو يقابل الموضوع لا المستعمل.",
     "en": "What is well known in the speech of the grammarians is [the division into] “neglected” (muhmal) or “used” (mustaʿmal). He departed from “neglected” because the neglected is that which has not been coined, and it is the counterpart of the coined (mawḍūʿ), not of the used."},
    {"type": "pair",
     "ar": "وكأنهم قصدوا بالمستعمل ما أمكن استعماله، وبالمهمل ما لم يمكن استعماله، وما ذكره أولى؛ لأن المتبادر من المستعمل المستعمل بالفعل.",
     "en": "It is as though they intended by “used” that whose use is possible, and by “neglected” that whose use is not possible; and what he mentioned is preferable, because what comes to mind first from “used” is that which is actually in use."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قيل: إنما صح إطلاق اللفظ على المركب من الحروف؛ لأنه في الأصل مصدر.",
     "en": "It is said: predicating “lafẓ” (utterance) of the compound [made] of letters is valid only because it is originally a verbal noun (maṣdar)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لا يخفى أنه إذا وضع اللفظ لما يتلفظ به الإنسان حقيقة أو حكما، فالمستكن في «اضرب» أيضا لفظ حقيقي، فالصواب: والمتلفظ به الحقيقي.",
     "en": "It is not hidden that, if “utterance” is coined for that which a human articulates whether really or constructively, then the concealed [pronoun] (al-mustakinn) in “iḍrib” is likewise a real utterance; so the correct [formulation] is: “and the really articulated” (al-mutalaffaẓ bihi al-ḥaqīqī)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قيل: ترك مثال الحرف اكتفاء بالكاف أو الواو في «زيد وضرب»، لكن لا يخفى ما بعده.",
     "en": "It is said: he omitted the example of the particle (ḥarf), contenting himself with the kāf or the wāw in “Zayd wa-ḍaraba”; but what follows [that view] is not hidden [in its weakness]."},
    {"type": "pair",
     "ar": "ويمكن أن يقال: ليس مقصوده ذكر جميع الأقسام كلها حتى يجب مثال الحرف أيضا، بل المراد أن يذكر مثال اللفظ الحقيقي والحكمي، وأن يبين أن الألفاظ التي في «زيد ضرب» بعضها حقيقي وبعضها حكمي.",
     "en": "One may say: his aim is not to mention every one of the divisions, such that the example of the particle too would be required; rather what is intended is to give an example of the real utterance and of the constructive one, and to make clear that among the utterances in “Zaydun ḍaraba” some are real and some are constructive."},
    {"type": "pair",
     "ar": "فقال: إن «زيد» و«ضرب» في «زيد ضرب» لفظ حقيقي، والمستكن تحت «ضرب» لفظ حكمي.",
     "en": "So he said: “Zayd” and “ḍaraba” in “Zaydun ḍaraba” are a real utterance, while the [pronoun] concealed beneath “ḍaraba” is a constructive utterance."},
    {"type": "pair",
     "ar": "فعلى هذا يكون قوله: في «زيد ضرب» ظرفا لمجموع قوله: «واللفظ الحقيقي واللفظ الحكمي» لا الثاني فقط، لما هو الظاهر.",
     "en": "On this basis, his statement “in Zaydun ḍaraba” is an adverbial [qualifier] governing the whole of his statement “the real utterance and the constructive utterance,” not the second only — this being the apparent [reading]."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الذي هو أعم من الحرف. ولا أدري أنه من أي مقولة هو؟",
     "en": "[The sound] which is more general than the particle. I do not know of which category it is."},
    {"type": "pair",
     "ar": "قال المصنف في شرح الإيضاح: إن المستتر هو المحذوف، لكن عبر عن المحذوف الذي هو الفاعل بالمستكن صونا للسان عن حذف الفاعل.",
     "en": "The author said in his commentary on al-Īḍāḥ: the hidden [pronoun] (al-mustatir) is the elided (al-maḥdhūf); but he expressed the elided — which is the agent (fāʿil) — by [the term] “concealed” (al-mustakinn), to guard the tongue from [saying] “elision of the agent.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: للمنوي.",
     "en": "That is: for the implied [pronoun] (al-manwī)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "فليس في «اضرب» إلا الفاعل المعقول من غير أن يكون فاعل ملفوظ. واكتفي بفهمه من غير لفظ اعتبار لفظ، فأقيم مقام اللفظ في اعتباره جزء الكلام الملفوظ أيضا، لجعله جزء الكلام المعقول.",
     "en": "So in “iḍrib” there is only the intelligible agent, without there being any articulated agent. He contented himself with its being understood without an utterance — [treating this] as a consideration of an utterance — so it was set in the place of the utterance, in that one regards it as a part of the articulated speech as well, [thereby] making it a part of the intelligible speech."},
    {"type": "pair",
     "ar": "فهو ليس من مقولة معينة، بل تارة يكون واجبا، وتارة يكون ممكنا جسما أو عرضا، وتارة يكون من مقولة الصوت إذا رجع الضمير إلى الصوت.",
     "en": "Thus it is not of a determinate category; rather, sometimes it is [a] necessary [being], sometimes possible — a body or an accident — and sometimes it is of the category of sound, when the pronoun refers back to a sound."},
    {"type": "pair",
     "ar": "قوله: «ليس من مقولة الحرف والصوت» أصلا ليس على ما ينبغي، فاحفظه؛ فإنه مما خفي على غيري حتى قال بعض الفضلاء: لا أدري من أي مقولة هو؟ فليت قولي بلغه.",
     "en": "His statement “it is not of the category of ḥarf and ṣawt” at all is not as it ought to be, so retain this; for it is among what was hidden from others, until one of the learned said: “I do not know of which category it is.” Would that my words had reached him."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "لما توهم أن مثل لفظ «هو» و«أنت» ليتحقق ذلك المنوي، فكيف يكون له لفظ؟ فدفع بأن المنفصل بني لتحقق ضمير المنفصل، لكنه قد يستعار ذلك المنفصل له.",
     "en": "Since it might be supposed that the like of the utterance “huwa” and “anta” [is what realizes] that implied [pronoun] — so how could it have an utterance? — he answered that the detached [pronoun] was coined to realize the detached pronoun, but that detached [form] is sometimes borrowed for it [the implied one]."},
    {"type": "pair",
     "ar": "وقد يقال: إن هذا القول تأييد أنه لم يبن له لفظ. والمعنى: أنه لو وضع لفظ لكان التعبير عنه بهذا اللفظ، لكنه يعبر عنه باستعارة لفظ المنفصل له، فلم يوضع له لفظ.",
     "en": "It may also be said: this statement corroborates that no utterance was coined for it. The meaning is: had an utterance been coined, the expression of it would be by this utterance; but rather it is expressed by borrowing the detached utterance for it, so no utterance was coined for it."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "للمنوي في «زيد ضرب»، و«أنت» للمنوي في «اضرب».",
     "en": "[“Huwa” is] for the implied [pronoun] in “Zaydun ḍaraba,” and “anta” for the implied [pronoun] in “iḍrib.”"},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "أي: على ذلك المنوي من كونه مسندا إليه، ومؤكدا، ومعطوفا عليه، إلى غير ذلك.",
     "en": "That is: [they applied] to that implied [pronoun] [the rulings] of its being that to which predication is made (musnad ilayhi), an emphasized term (muʾakkad), that upon which conjunction is made (maʿṭūf ʿalayhi), and so forth."},
    {"type": "pair",
     "ar": "قوله: «وأجروا عليه» عطف على قوله: «ليس من مقولة الحرف والصوت» لا على قوله: «عبروا عنه»؛ إذ المقصود منه إثبات حكمية المنوي لا دفع التوهم المذكور، وكبراه مطوية.",
     "en": "His statement “and they applied to it” is conjoined to his statement “it is not of the category of ḥarf and ṣawt,” not to his statement “they expressed it”; for what is intended by it is establishing the constructive [utterance-]status of the implied [pronoun], not repelling the aforementioned supposition — its major premise being left implicit (maṭwiyya)."},
    {"type": "pair",
     "ar": "تقريره بطريق الشكل الأول: أن المنوي أمر أجروا عليه أحكام اللفظ، وكل ما أجري عليه أحكام اللفظ فهو اللفظ حكما، فالمنوي لفظ حكما.",
     "en": "Its exposition, by way of the first figure [of the syllogism], is: the implied [pronoun] is a thing to which they applied the rulings of the utterance; and everything to which the rulings of the utterance are applied is an utterance by [legal] status; therefore the implied [pronoun] is an utterance by status."},
]
