# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 250 (printed ٢٤٩)."""

PAGE_NUMBER = 250
PRINTED_PAGE = "٢٤٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «أي: من حيث هو فاعل أو مفعول به، كما هو الظاهر،» from the foot of PDF p. 249.
    {"type": "matn",
     "ar": "فبذكر الهيئة يخرج ما يبين الذات كالتمييز،",
     "en": "…so by the mention of “state” (hayʾa) there is excluded what clarifies the essence, such as the specification (tamyīz);"},
    {"type": "matn",
     "ar": "وبإضافتها إلى الفاعل أو المفعول به يخرج ما يبين هيئة غير الفاعل أو المفعول به كصفة المبتدأ، نحو: «زيد العالم أخوك»،",
     "en": "by annexing it to the agent or the direct object there is excluded what clarifies the state of something other than the agent or the direct object, such as the adjective of the mubtadaʾ, as in “Zayd the learned is your brother”;"},
    {"type": "matn",
     "ar": "وبقيد الحيثية يخرج صفة الفاعل أو المفعول به، فإنها تدل على هيئة الفاعل أو المفعول به مطلقا، لا من حيث هو فاعل أو مفعول،",
     "en": "and by the qualification “inasmuch as” (ḥaythiyya) there is excluded the adjective of the agent or the direct object, for it indicates the state of the agent or the direct object absolutely, not inasmuch as it is an agent or an object."},
    {"type": "matn",
     "ar": "وهذا الترديد على سبيل منع الخلو لا الجمع[[١]]، فلا يخرج منه مثل: «ضرب زيد عمرا راكبين»[[٢]].",
     "en": "This disjunction is by way of excluding the absence of both (manʿ al-khulūw), not excluding their conjunction (manʿ al-jamʿ); so an example such as “Zayd struck ʿAmr, both riding” is not excluded by it."},
    {"type": "matn",
     "ar": "(لفظا) أي: سواء كان الفاعل أو المفعول الذي وقع الحال عنه لفظا أي: لفظيا",
     "en": "(Verbally), that is, whether the agent or the object from which the ḥāl occurs is so verbally, that is, verbally determined (lafẓī),"},
    {"type": "matn",
     "ar": "بأن يكون[[٣]] فاعلية الفاعل أو مفعولية المفعول باعتبار لفظ الكلام، ومنطوقه من غير اعتبار معنى خارج عنه يفهم من فحوى الكلام، سواء كانا ملفوظين حقيقة أو حكما.",
     "en": "in that the agent’s being an agent or the object’s being an object is by consideration of the wording of the speech and what it explicitly expresses, without regard to a meaning outside it understood from the purport (faḥwā) of the speech—whether the two are uttered actually or virtually."},
    {"type": "matn",
     "ar": "(أو معنى[[٤]]) أي: معنويا بأن يكون فاعلية الفاعل أو مفعولية المفعول باعتبار معنى يفهم من فحوى الكلام لا باعتبار لفظه ومنطوقه.",
     "en": "(Or in meaning), that is, semantically determined (maʿnawī), in that the agent’s being an agent or the object’s being an object is by consideration of a meaning understood from the purport of the speech, not by consideration of its wording and explicit expression."},
    {"type": "matn",
     "ar": "والمراد بالفاعل أو المفعول أعم من أن يكون حقيقة أو حكما، فيدخل فيه الحال عن المفعول معه، لكونه في معنى الفاعل أو المفعول به.",
     "en": "What is meant by “agent” or “object” is more general than its being so actually or virtually; so there enters into it the ḥāl of the concomitant object (mafʿūl maʿahu), since it has the sense of the agent or the direct object."},
    {"type": "matn",
     "ar": "وكذا المفعول المطلق مثل: «ضربت الضرب شديدا»، فإنه بمعنى: «أحدثت الضرب شديدا»،",
     "en": "Likewise the absolute object (mafʿūl muṭlaq), as in “I struck the striking severe,” for it means “I produced the striking severe.”"},
    {"type": "matn",
     "ar": "وكذا يدخل فيه الحال عن المضاف إليه، كما إذا كان المضاف فاعلا أو مفعولا يصح حذفه، وقيام المضاف إليه مقامه، فكأنه الفاعل أو المفعول به[[٥]]",
     "en": "Likewise there enters into it the ḥāl of the second term of a genitive construction (muḍāf ilayhi), as when the first term (muḍāf) is an agent or an object whose omission is valid, with the muḍāf ilayhi standing in its place, so that it is as though it were the agent or the direct object,"},
    {"type": "matn",
     "ar": "نحو: ﴿بل ملة إبراهيم حنيفا﴾[[٦]]،",
     "en": "as in: “Nay, the creed of Abraham, a ḥanīf”;…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: print reads «جاز التعريف» («definition»); the sense (contrasted with «الجمع») requires «التفريق» (separation). Transcribed as printed.
    {"type": "pair",
     "ar": "إذا توافقت حال الفاعل والمفعول جاز التعريف كقولك: «ضربت راكبا زيدا راكبا»، والجمع كقولك: «لقيت زيدا راكبين».",
     "en": "When the ḥāl of the agent and that of the object agree, separation [reading tafrīq for the printed taʿrīf] is permitted—as when you say “Riding, I struck Zayd riding”—and so is combination, as when you say “I met Zayd, both riding.”"},
    {"type": "pair",
     "ar": "وإذا اختلفتا فإن كان هناك قرينة يعرف بها صاحب كل واحد منهما جاز وقوعهما كيف ما كانا نحو: «لقيت هندا مصعدا منحدرة»،",
     "en": "When they differ, then if there is a contextual indicator (qarīna) by which the owner of each of them is known, their occurrence is permitted in whatever order they come, as in “I met Hind, [I] ascending, [she] descending.”"},
    {"type": "pair",
     "ar": "وإن لم تكن فالأولى جعل كل واحد منهما بجنب صاحبه، نحو: «لقيت منحدرا زيدا مصعدا»،",
     "en": "If there is none, it is preferable to place each of them beside its owner, as in “Descending, I met Zayd ascending.”"},
    {"type": "pair",
     "ar": "ويجوز على ضعف جعل حال المفعول بجنبه، وتأخير حال الفاعل ليقع أحد الحالين بجنب صاحبه، هكذا قال الشيخ الرضي.",
     "en": "It is permitted, weakly, to place the ḥāl of the object beside it and to defer the ḥāl of the agent, so that one of the two ḥāls falls beside its owner; so said Shaykh al-Raḍī."},
    {"type": "pair",
     "ar": "وقال بعض شراح المفصل: حق الحال المفرقة أن ترتب على حد ترتيب صاحبها.",
     "en": "One of the commentators on al-Mufaṣṣal said: the due of separated ḥāls is that they be ordered according to the order of their owners."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: print reads «وعمر راكبا» (not «عمرا»); transcribed as printed.
    {"type": "pair",
     "ar": "يجوز فيه «ضرب زيد راكبا وعمر راكبا».",
     "en": "In it, “Zayd, riding, struck ʿAmr, riding” is permitted."},
    {"type": "pair",
     "ar": "وأما إذا تخالفت حال الفاعل أو المفعول، فلا بد من التفريق،",
     "en": "But when the ḥāl of the agent and that of the object differ, separation is necessary;"},
    {"type": "pair",
     "ar": "فإن لم يكن قرينة فالأولى جعل كل منهما بجنب صاحبها. وقد يذكر على سبيل اللف والنشر المرتب.",
     "en": "and if there is no contextual indicator, it is preferable to place each of them beside its owner. It may also be stated by way of ordered convolution and unfolding (al-laff wa-l-nashr al-murattab)."},
    {"type": "pair",
     "ar": "وقيل: حقه هذا وقد جاء على ضعف جعل حال المفعول بجنبه، وتأخير حال الفاعل.",
     "en": "It has been said: this is its due; and placing the ḥāl of the object beside it and deferring the ḥāl of the agent has occurred, weakly."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يرشدك إلى هذا تفصيل العامل.",
     "en": "The detailed treatment of the governing element (ʿāmil) guides you to this."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "تمييز عن الفاعل والمفعول، أو حال عنهما، أو خبر لـ«كان» المقدر كما أشار إليه في الشرح.",
     "en": "[It is] a specification (tamyīz) relating to the agent and the object, or a ḥāl of them, or the predicate of an implied “kāna,” as he indicated in the commentary."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فإن تعلق فعل شخص بمفهومين علامة اتحادهما ذاتا.",
     "en": "For the connection of one person’s action with two concepts is a sign that the two are one in essence."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "سورة البقرة: ١٣٥.",
     "en": "Qurʾān, Sūrat al-Baqara 2:135."},
]
