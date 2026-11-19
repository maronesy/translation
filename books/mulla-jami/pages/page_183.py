# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 183 (printed ١٨٢)."""

PAGE_NUMBER = 183
PRINTED_PAGE = "١٨٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "في، أو مع، أو اللام» بخلاف المفاعيل الأربعة الباقية[[١]]،",
     "en": "…“fī,” or “maʿa,” or the lām”—unlike the remaining four objects (mafāʿīl),"},
    {"type": "matn",
     "ar": "فإنه لا يصح إطلاق صيغة المفعول عليها[[٢]] إلا بعد تقييدها بواحدة منها، فيقال: «المفعول به، أو فيه، أو معه، أو له».",
     "en": "for the form “object” cannot validly be applied to them except after restricting it by one of these; so one says: “the object to which [the act is done]” (al-mafʿūl bihi), or “in which” (fīhi), or “with which” (maʿahu), or “for which” (lahu)."},
    {"type": "matn",
     "ar": "(وهو) أي: المفعول المطلق (اسم ما فعله فاعل[[٣]] فعل)",
     "en": "(And it)—that is, the absolute object—(is the noun of what the agent of a verb did),"},
    {"type": "matn",
     "ar": "والمراد بفعل الفاعل إياه، قيامه به بحيث يصح إسناده إليه[[٤]]، لا أن يكون مؤثرا فيه[[٥]] موجدا إياه،",
     "en": "What is meant by the agent’s doing it is its subsisting in him such that it can validly be predicated of him—not that he exerts causal influence on it, bringing it into existence."},
    {"type": "matn",
     "ar": "فلا[[٦]] يرد عليه مثل: «مات موتا[[٧]]، وجسم جسامة، وشرف شرفا»،",
     "en": "So such as “he died a death” (māta mawtan), “he grew large in bulk” (jasuma jasāmatan) and “he was noble with nobility” (sharufa sharafan) do not constitute an objection to it."},
    {"type": "matn",
     "ar": "وإنما زيد لفظ الاسم[[٨]]؛",
     "en": "The word “noun” (ism) was added only…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "حصر النحاة المفاعيل في الخمسة.",
     "en": "The grammarians restricted the objects to five."},
    {"type": "pair",
     "ar": "وقال الشيخ الرضي: يجوز أن يجعل الحال داخلة في المفاعيل، فقال للحال: هو مفعول مع قيد مضمونه؛",
     "en": "Shaykh al-Raḍī said: the circumstantial (ḥāl) may be counted among the objects; and he said of the ḥāl: it is an object together with the qualification of its content;"},
    {"type": "pair",
     "ar": "إذ المجيء في «جاءني زيد راكبا» فعل مع قيد الركوب الذي هو مضمون راكبا.",
     "en": "since the coming in “Zayd came to me riding” (jāʾanī Zaydun rākiban) is an act together with the qualification of riding, which is the content of “rākiban.”"},
    {"type": "pair",
     "ar": "ويقال للمستثنى: هو المفعول بشرط إخراجه، وكأنهم آثروا التخفيف في التسمية، انتهى.",
     "en": "And of the excepted [noun] (mustathnā) it is said: it is the object on condition of its being excluded; and it is as though they preferred brevity in naming. End [of quotation]."},
    {"type": "pair",
     "ar": "ولا يبعد أن يقال: إن المفعول ما يتعلق به الفعل أولا وبالذات، والحال ليست كذلك؛ لأن تعلقها به بواسطة أنها مبينة لهيئة فاعله أو مفعوله.",
     "en": "It is not far-fetched to say that an object is that with which the verb is connected primarily and essentially, and the ḥāl is not so, because its connection with it is by means of its specifying the state (hayʾa) of its agent or its object."},
    {"type": "pair",
     "ar": "وكذا المستثنى لأن تعلقه به بواسطة أنه مخرج عن أمر يقع معموله على سبيل الاتفاق.",
     "en": "Likewise the excepted noun, because its connection with it is by means of its being excluded from something that happens to be its governed element."},
    {"type": "pair",
     "ar": "ومن ههنا أعني: من أن تعلق المفاعيل بالفعل بالذات، وتعلق غيرها بالواسطة، يظهر توجيه جعل النصب في المفاعيل أصلا، وفي غيرها تبعا.",
     "en": "From this—I mean, from the fact that the objects are connected with the verb essentially and the others by an intermediary—the rationale for making the accusative original in the objects and derivative in the others becomes clear."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: لا يصح إطلاق المفعول اللغوي عليها، فلا ينافي إطلاق المفعول العرفي على الخمسة.",
     "en": "That is: “object” in its lexical sense cannot validly be applied to them; so this does not conflict with the application of “object” in its conventional (ʿurfī) sense to the five."},
    {"type": "pair",
     "ar": "إن قلت: من ضرورات صدق المقيد صدق المطلق، فكيف يصح القول بصدق المقيد، وامتناع صدق المطلق؟",
     "en": "If you say: the truth of the restricted [term] necessarily entails the truth of the unrestricted; so how can one validly hold that the restricted is true while the unrestricted cannot be?"},
    {"type": "pair",
     "ar": "قلنا: مطلق هذه المقيدات معنى يشمل «به، وله، وفيه، ومعه» لا المفعول كما في «زيد حسن الغلام».",
     "en": "We say: the unrestricted [term] of these restricted ones is a meaning that covers “bihi,” “lahu,” “fīhi” and “maʿahu,” not “the object” [as such]—as in “Zayd is of handsome servant” (Zaydun ḥasanu al-ghulāmi)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "حقيقة أو حكما. فدخل فيه «ضرب ضربا» على صيغة المجهول.",
     "en": "Really or by assimilated status. So “ḍuriba ḍarban” (a beating was beaten), in the passive form, is included in it."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: على تقدير: إن كان مثبتا أو سواء كان بطريق النفي أو الإثبات،",
     "en": "That is: on the supposition [that it is so predicated] if it is affirmative; or [the predication holds] whether by way of negation or affirmation;"},
    {"type": "pair",
     "ar": "فلا يبطل الطرد بمثل «ما ضربت ضربا شديدا».",
     "en": "so the exclusiveness [of the definition] (ṭard) is not invalidated by such as “I did not beat a severe beating” (mā ḍarabtu ḍarban shadīdan)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "كما ذهب إليه بعضهم، فيشكل عليه دخول الأمثلة الآتية.",
     "en": "As some held; but then the inclusion of the examples that follow becomes problematic for him."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "تفريع على قوله: والمراد إلى آخره، أي: لا يرد على التعريف أنه غير جامع، ففيه رد للفاضل الهندي.",
     "en": "[This is] a consequence drawn from his words “What is meant …” to the end; that is: the objection does not arise against the definition that it is not comprehensive (jāmiʿ). In this there is a rejoinder to al-Fāḍil al-Hindī."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "وكذا «ضرب زيد ضربا» على صيغة المجهول؛ لأنه فعله بمعنى أنه قام بفاعل معنى الفعل المذكور، أي: بما قام به معنى الفعل المذكور،",
     "en": "Likewise “Zayd was beaten a beating” (ḍuriba Zaydun ḍarban), in the passive form; because it is his act in the sense that it subsisted in the agent of the meaning of the mentioned verb—that is, in that in which the meaning of the mentioned verb subsists."},
    {"type": "pair",
     "ar": "فلا حاجة مع هذا التفسير إلى جعل الفاعل أعم من الفاعل حقيقة أو حكما، ليدخل فيه مثل: «ضرب زيد ضربا»، كما ظن البعض بعض الظن.",
     "en": "So with this explanation there is no need to make “agent” more general [so as to cover] the agent in reality or by assimilated status, in order that such as “ḍuriba Zaydun ḍarban” be included in it, as some have [mistakenly] supposed."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "ما ذكره في وجه زيادة الاسم واضح لا مرية فيه، إنما الشأن في تخصيص المفعول المطلق بزيادة الاسم في تعريفه دون أخواته،",
     "en": "What he mentioned concerning the reason for adding “noun” is clear, with no doubt about it; the issue lies only in singling out the absolute object for the addition of “noun” in its definition, to the exclusion of its sisters."},
    {"type": "pair",
     "ar": "فلذا احتيج إلى ما قيل: إن زيادته لإخراج ضرب الثاني في «ضرب ضرب زيد»، فإن ضرب الثاني ما فعله فاعل فعل مذكور.",
     "en": "For this reason recourse was had to what has been said: that its addition is to exclude the second “ḍaraba” in “ḍaraba ḍaraba Zaydun,” for the second “ḍaraba” is what the agent of a mentioned verb did."},
    {"type": "pair",
     "ar": "ويتجه عليه أمران:",
     "en": "Two points are raised against this:"},
    {"type": "pair",
     "ar": "أحدهما: ما قيل: إن ضرب الثاني ليس ما فعله الفاعل؛ لأنهم لا يجرون صفات المعاني التضمنية على الألفاظ، وإنما يجرون صفات المعاني المطابقية.",
     "en": "The first is what has been said: that the second “ḍaraba” is not what the agent did, because they do not apply the attributes of implied (taḍammunī) meanings to words; they apply only the attributes of meanings by full correspondence (muṭābaqī)."},
    {"type": "pair",
     "ar": "وثانيهما: ما تقول: إنه لا ينفع لإخراج «زيد ضارب ضارب».",
     "en": "The second is what you [may] say: that it is of no use for excluding “Zaydun ḍāribun ḍāribun.”"},
    {"type": "pair",
     "ar": "فالوجه أن يقال: زيادة الاسم ههنا وتركه في أخواته تفنن في البيان، والشارح جعل الاسم محذوفا في تعريفات أخواته اكتفاء بذكره في تعريفه.",
     "en": "The correct approach is to say: adding “noun” here and omitting it in its sisters is stylistic variation in expression (tafannun fī al-bayān); and the commentator took “noun” to be elided in the definitions of its sisters, being content with its mention in its [own] definition."},
]
